

import os
import pwd
import subprocess
from pathlib import Path
import sys
import stat
from typing import Union

scriptDir = Path(os.path.dirname(os.path.realpath(__file__)))
gitRootDir = Path(os.path.dirname(scriptDir))

PathOrStr = Union[str,Path]

class User(object):

    def __init__(self, login: str, authorizedKeys: list[str] = []):
        self.username = login
        self.login = login
        self.name = login
        self.pwname = pwd.getpwnam(login)
        self.home = os.path.expanduser( f"~{login}")
        self.pw_uid = self.pwname.pw_uid
        self.pw_gid = self.pwname.pw_gid
        self.authorizedKeys = authorizedKeys

    def homePathStr(self, pathname: PathOrStr) -> str:
        return os.path.join(self.home, pathname)

    def homePath(self, pathname: PathOrStr) -> Path:
        return Path(os.path.join(self.home, pathname))

    def writeInHome(self, filename: PathOrStr, contents: str) -> str:
        absoluteFilename = os.path.join(self.home, filename)
        self.writeFile(absoluteFilename, contents)
        return absoluteFilename

    def execAsUser(self, args: (str | list[str]), cwd=None) -> None:

        if cwd is None:
            cwd = self.home

        if isinstance(args, str):
            args = [args]

        if not self.username == os.getlogin():
            args = ["sudo", "-u", self.username] + args

        print(f"exec - " + str(args) + "  cwd=" + str(cwd))
        completedProcess = subprocess.run(args, cwd=cwd)
        if completedProcess.returncode != 0:
            print("exec failed with exitcode " + str(completedProcess.returncode))
            sys.exit(1)

    def pathExists(self, path: PathOrStr) -> bool:
        absolutePath = os.path.join(self.home, path)
        return os.path.exists(absolutePath)

    def runContents(self, name: str, scriptContents: str) -> None:
        scriptFile = self.writeInHome(f"temp-script-{name}.sh", scriptContents)
        st = os.stat(scriptFile)
        os.chmod(scriptFile, st.st_mode | stat.S_IEXEC)
        self.execAsUser(scriptFile)
        self.deleteFile(scriptFile)

    def deleteFile(self, filename):
        self.execShell(f"rm {filename}")

    def chownPath(self, path: PathOrStr) -> None:
        os.chown(path, self.pw_uid, self.pw_gid)

    def writeFile(self, filename: str, contents: str):
        parent = os.path.dirname(filename)
        self.makeDirectories(parent)
        out = open(filename, "w")
        out.write(contents)
        out.close()
        os.chown(filename, self.pw_uid, self.pw_gid)

    def makeDirectories(self, directory: PathOrStr):
        directory = str(directory)
        if not os.path.exists(directory):
            self.execAsUser(["mkdir", "-p", directory])

    def installNix(self):
        if not os.path.exists("/nix"):
            # self.execShell("""find /etc -name '*.backup-before-nix' | xargs rm -rf""")
            installScript = f"{self.home}/temp-nix-install.sh"
            self.execShell(f"curl -L https://nixos.org/nix/install | sudo -u {self.name} tee {installScript} > /dev/null")
            # nohup because we have to run the install script without a tty so it doesn't prompt us
            self.execShell(f"nohup sh {installScript} --daemon | cat")
            self.deleteFile(installScript)

    def homeManagerSwitch(self):
        self.installNix()
        homeManagerDir = gitRootDir / "home-manager"
        self.execAsUser(f"{homeManagerDir}/switch.sh", cwd=homeManagerDir)

    def execShell(self, command, cwd=None):
        print("execShell - " + command)

        if not self.username == os.getlogin():
            command = f"sudo -u {self.username} {command}"

        subprocess.check_output(command, shell=True, cwd=cwd)

    def copyFile(self, fromFile: Union[str, Path], toFile: Union[str, Path]) -> None:
        import shutil
        toParent = os.path.dirname(toFile)
        self.makeDirectories(toParent)
        shutil.copyfile(fromFile, toFile)
        os.chown(toFile, self.pw_uid, self.pw_gid)


    def generateAuthorizedKeys2(self) -> None:
        authorizedKeys2Contents = "\n".join([key for key in self.authorizedKeys])
        filename = self.writeInHome(".ssh/authorized_keys2", authorizedKeys2Contents)
        os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR)
        sshDir = os.path.dirname(filename)
        os.chmod(sshDir, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)



