

import os
import pwd
import subprocess


class User(object):

    def __init__(self, username: str):
        self.username = username
        self.login = username
        self.name = username
        self.pwname = pwd.getpwnam(username)
        self.home = os.path.expanduser( f"~{username}")
        self.pw_uid = self.pwname.pw_uid
        self.pw_gid = self.pwname.pw_gid

    def writeInHome(self, filename: str, contents: str) -> str:
        absoluteFilename = os.path.join(self.home, filename)
        self.writeFile(absoluteFilename, contents)
        return absoluteFilename

    def execAsUser(self, args: (str | list[str]), **kwargs) -> None:
        cwd = kwargs.cwd
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

    def pathExists(self, path: str) -> bool:
        absolutePath = os.path.join(self.home, path)
        return os.path.exists(absolutePath)

    def runContents(self, name: str, scriptContents: str) -> None:
        scriptFile = self.writeInHome(f"temp-script-{name}.sh", scriptContents)
        st = os.stat(scriptFile)
        os.chmod(scriptFile, st.st_mode | stat.S_IEXEC)
        self.execAsUser(scriptFile)
        deleteFile(scriptFile)

    def writeFile(self, filename: str, contents: str):
        parent = os.path.dirname(filename)
        self.makeDirectories(parent)
        out = open(filename, "w")
        out.write(contents)
        out.close()
        os.chown(filename, self.pw_uid, self.pw_gid)

    def makeDirectories(self, directory: str):
        if not os.path.exists(directory):
            self.execAsUser("mkdir", "-p", directory)

    def installNix(self):
        if not os.path.exists("/nix"):
            execShell("""find /etc -name '*.backup-before-nix' | xargs rm -rf""")
            installScript = f"{user.home}/temp-nix-install.sh"
            execShell(f"curl -L https://nixos.org/nix/install | sudo -u {user.name} tee {installScript} > /dev/null")
            user.execAsUser("sh", installScript, "--daemon")
            deleteFile(installScript)

    def homeManagerSwitch(self):
        homeManagerDir = f"{scriptDir}/home-manager"
        self.execAsUser(f"{homeManagerDir}/switch.sh", cwd=homeManagerDir)

    def execShell(self, command, cwd=None):
        print("execShell - " + command)

        if not self.username == os.getlogin():
            command = f"sudo -u {self.username} {command}"

        subprocess.check_output(command, shell=True, cwd=cwd)

