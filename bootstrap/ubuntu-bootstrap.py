#!/usr/bin/env python3


import subprocess
import os
import sys
from pathlib import Path
import stat
import pwd
from pathlib import Path
from User import User
from typing_extensions import TypedDict

scriptDir = Path(os.path.dirname(os.path.realpath(__file__)))
gitRootDir = Path(os.path.dirname(scriptDir))


Repository = TypedDict(
        "Repository",
        {
            "name": str,
            "file": str,
            "source": str,
        }
    )

Config = TypedDict(
        "Config", 
        {
            "hostname": str,
            "zerotierNetworkId": str,
            "repositores": list[Repository],
            "standalonePackages": list[str],
            "rsnapshot": list[str],
        }
    )

config: Config = {
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
        "caddy",
        "supervisor",
    ],
    "rsnapshot": [
        "/etc/",
        "/home/",
        "/root/",
    ],
}


aptUpdateNeeded = False

def setupRepos() -> None:
    for repo in config["repositores"]:
        name = repo["name"]
        file = repo["file"]
        source = repo["source"]
        if not os.path.exists(file):
            root.execAsUser(["apt-add-repository", "-y", source])
            aptUpdateNeeded = True
        else:
            print(f"repo {name} already setup")    


def setHostname(hostname: str) -> None:
    import socket
    existingHostname = socket.gethostname()
    if existingHostname != hostname:
        root.execAsUser(["hostnamectl", "set-hostname", hostname])
    else:
        print(f"hostname already set to {hostname}")


def aptUpdate() -> None:
    global aptUpdateNeeded
    if aptUpdateNeeded:
        root.execAsUser(["apt", "update"])
        aptUpdateNeeded = False


def installPackages(*packages: str) -> None:
    if not arePackagesInstalled(*packages):
        packagesL = list(packages)
        print("installing packages -- " + str(packagesL))
        root.execAsUser(["apt", "install", "-y"] + packagesL)
    else:
        print("packages already installed -- " + str(list(packages)))



def setupCaddyRepo() -> None:
    global aptUpdateNeeded
    installPackages("debian-keyring", "debian-archive-keyring", "apt-transport-https")
    if not os.path.exists("/usr/share/keyrings/caddy-stable-archive-keyring.gpg"):
        root.execShell("curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor > /usr/share/keyrings/caddy-stable-archive-keyring.gpg")
    if not os.path.exists("/etc/apt/sources.list.d/caddy-stable.list"):        
        root.execShell("curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list")
        aptUpdateNeeded = True


def setupZerotier() -> None:
    if not os.path.exists("/usr/sbin/zerotier-cli"):
        root.execShell("curl -s https://install.zerotier.com | sudo bash")
        root.execAsUser(["zerotier-cli", "join", config["zerotierNetworkId"]])
    else:
        print("zerotier already installed")    


def configureCaddy() -> None:
    if not root.pathExists("/etc/caddy/apps-setup-complete"):
        root.copyFile(scriptDir / "Caddyfile", "/etc/caddy/Caddyfile")
        root.writeFile("/etc/caddy/apps-setup-complete", "do nothing / noop marker file to show that apps have been setup")
        root.makeDirectories("/etc/caddy/apps/")
        root.execAsUser(["systemctl", "enable", "--now", "caddy"])


def configureSupervisor() -> None:
    if not root.pathExists("/etc/supervisor/conf.d/apps.conf"):
        root.copyFile(scriptDir / "supervisor-apps.conf", "/etc/supervisor/conf.d/apps.conf")
        root.makeDirectories("/etc/supervisor/apps/")



def createSudoUser(username: str) -> User:
    if not userExists(username):
        root.execAsUser(["adduser", "--disabled-password", "--gecos", "", username])
    root.writeFile(f"/etc/sudoers.d/{username}", f"{username} ALL=(ALL) NOPASSWD: ALL")
    return User(username)

def userExists(username: str) -> bool:
    import pwd
    try:
        pwd.getpwnam(username)
        return True
    except KeyError:
        return False


def deleteFile(file: Path) -> None:
    if os.path.exists(file):
        print(f"deleting -- {file}")
        os.remove(file)
    else:
        print(f"not deleting because it doesn't exist -- {file}")


def arePackagesInstalled(*packages: str) -> bool:
    import apt
    cache = apt.Cache()
    def isPackageInstalled(package): 
        return cache.get(package) is not None
    return all(isPackageInstalled(p) for p in packages)
    


def installEtcKeeper() -> None:
    global aptUpdateNeeded
    if not arePackagesInstalled("etckeeper"):
        aptUpdateNeeded = True
        aptUpdate()
        installPackages("etckeeper")



root = User("root")

installEtcKeeper()
setHostname(config["hostname"])

setupRepos()
setupCaddyRepo()

aptUpdate()

installPackages(*config["standalonePackages"])

setupZerotier()

configureCaddy()
configureSupervisor()


devUser = createSudoUser("dev")

devUser.homeManagerSwitch()

print("successfully completed")


# setup for use as a server_sync_apps

# setup for rsnapshot (add rsnapshot keys for ssh into root)


