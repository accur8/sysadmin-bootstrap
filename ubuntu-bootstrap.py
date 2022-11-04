#!/usr/bin/env python3


import subprocess
import os
import sys
from pathlib import Path
import stat
import pwd


scriptDir = os.path.dirname(os.path.realpath(__file__))

config = {
    "hostname": "orchid",
    "zerotierNetworkId": "8056c2e21cb31b0c",
    "repositores": [
        {
            "name": "fish shell",
            "file": "/etc/apt/sources.list.d/fish-shell-ubuntu-release-3-jammy.list",
            "source": "ppa:fish-shell/release-3"
        }
    ],
    "standalonePackages": [
        "fish",
        # "ncdu",
    ],
    "rsnapshot": [
        "/etc/",
        "/home/",
        "/root/",
    ],
}


aptUpdateNeeded = False


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

    def execAsUser(self, *args: str) -> None:
        exec(["sudo", "-u", self.username] + list(args), cwd=self.home)

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

def setupRepos():
    for repo in config["repositores"]:
        name = repo["name"]
        file = repo["file"]
        source = repo["source"]
        if not os.path.exists(file):
            exec(["apt-add-repository", "-y", source])
            aptUpdateNeeded = True
        else:
            print(f"repo {name} already setup")    


def setHostname(hostname):
    import socket
    existingHostname = socket.gethostname()
    if existingHostname != hostname:
        exec(["hostnamectl", "set-hostname", hostname])
    else:
        print(f"hostname already set to {hostname}")


def aptUpdate():
    global aptUpdateNeeded
    if aptUpdateNeeded:
        exec(["apt", "update"])
        aptUpdateNeeded = False


def installPackages(*packages: str):
    if not arePackagesInstalled(*packages):
        packages = list(packages)
        print("installing packages -- " + str(packages))
        exec(["apt", "install", "-y"] + packages)
    else:
        print("packages already installed -- " + str(packages))



def setupCaddyRepo():
    global aptUpdateNeeded
    installPackages("debian-keyring", "debian-archive-keyring", "apt-transport-https")
    if not os.path.exists("/usr/share/keyrings/caddy-stable-archive-keyring.gpg"):
        execShell("curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor > /usr/share/keyrings/caddy-stable-archive-keyring.gpg")
    if not os.path.exists("/etc/apt/sources.list.d/caddy-stable.list"):        
        execShell("curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list")
        aptUpdateNeeded = True


def installCaddy():
    if not arePackagesInstalled("caddy"):
        installPackages("caddy")
        exec(["systemctl", "enable", "--now", "caddy"])


def installSupervisor():
    installPackages("supervisor")


def execShell(cmd):
    print("execShell - " + cmd)
    subprocess.check_output(cmd, shell=True)


def exec(args, cwd=None):
    print("exec - " + str(args) + "  cwd=" + str(cwd))
    completedProcess = subprocess.run(args, cwd=cwd)
    if completedProcess.returncode != 0:
        print("exec failed with exitcode " + str(completedProcess.returncode))
        sys.exit(1)


def setupZerotier():
    if not os.path.exists("/usr/sbin/zerotier-cli"):
        execShell("curl -s https://install.zerotier.com | sudo bash")
        exec(["zerotier-cli", "join", config["zerotierNetworkId"]])
    else:
        print("zerotier already installed")    


def configureCaddy():
    root.writeFile(
        "/etc/caddy/Caddyfile",
        """
import /etc/caddy/apps/*
        """
    )
    root.makeDirectories("/etc/caddy/apps/")


def configureSupervisor():
    root.writeFile(
        "/etc/supervisor/conf.d/apps.conf",
        """
[include]
files = /etc/supervisor/apps/*.conf
        """
    )
    root.makeDirectories("/etc/supervisor/apps/")


def createSudoUser(username):
    if not userExists(username):
        exec(["adduser", "--disabled-password", "--gecos", "", username])
    root.writeFile(f"/etc/sudoers.d/{username}", f"{username} ALL=(ALL) NOPASSWD: ALL")


def installNix(user):
    if not os.path.exists("/nix"):
        execShell("""find /etc -name '*.backup-before-nix' | xargs rm -rf""")
        installScript = f"{user.home}/temp-nix-install.sh"
        execShell(f"curl -L https://nixos.org/nix/install | sudo -u {user.name} tee {installScript} > /dev/null")
        user.execAsUser("sh", installScript, "--daemon")
        deleteFile(installScript)


def installHomeManager(user):
    if not user.pathExists(".nix-profile/bin/home-manager"):
        nixPathSnippet = "${NIX_PATH:+:$NIX_PATH}"
        user.runContents(
            "install-home-manager",
            f"""#!/usr/bin/env bash

                # exit when any command fails
                set -e

                /nix/var/nix/profiles/default/bin/nix-channel --add https://github.com/nix-community/home-manager/archive/master.tar.gz home-manager

                /nix/var/nix/profiles/default/bin/nix-channel --update

                export NIX_PATH=$HOME/.nix-defexpr/channels:/nix/var/nix/profiles/per-user/root/channels{nixPathSnippet}

                echo installing home manager

                /nix/var/nix/profiles/default/bin/nix-shell '<home-manager>' -A install

            """
            )


def configureHomeManager(user: User) -> None:        
    writeHomeManagerConfig(user)
    user.runContents(
        "home-manager-switch",
        f"""#!/bin/sh

            export PATH=$PATH:~/.nix-profile/bin/:/nix/var/nix/profiles/default/bin/

            home-manager switch -b backup

        """
    )


def userExists(username: str) -> bool:
    import pwd
    try:
        pwd.getpwnam(username)
        return True
    except KeyError:
        return False


def deleteFile(file):
    if os.path.exists(file):
        print(f"deleting -- {file}")
        os.remove(file)
    else:
        print(f"not deleting because it doesn't exist -- {file}")


def arePackagesInstalled(*packages: str):
    import apt
    cache = apt.Cache()
    def isPackageInstalled(package): 
        return cache.get(package) is not None
    return all(isPackageInstalled(p) for p in packages)
    


def installEtcKeeper():
    global aptUpdateNeeded
    if not arePackagesInstalled("etckeeper"):
        aptUpdateNeeded = True
        aptUpdate()
        installPackages("etckeeper")


def homeManagerSwitch(user: User):


root = User("root")

installEtcKeeper()
setHostname(config["hostname"])

setupRepos()
setupCaddyRepo()

aptUpdate()

installPackages(*config["standalonePackages"])

installCaddy()  
installSupervisor()

setupZerotier()

configureCaddy()
configureSupervisor()


defUsername = "dev"

createSudoUser(defUsername)

devUser = User(defUsername)
installNix(devUser)
homeManagerSwitch(devUser)


print("successfully completed")


# setup for use as a server_sync_apps

# setup for rsnapshot (add rsnapshot keys for ssh into root)


