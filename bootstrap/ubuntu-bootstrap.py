#!/usr/bin/env python3


import subprocess
import os
import sys
from pathlib import Path
import stat
import pwd
from User import User
from typing import List

scriptDir = Path(os.path.dirname(os.path.realpath(__file__)))
gitRootDir = Path(os.path.dirname(scriptDir))


class UserConfig:
    def __init__(self, **kwargs):
        self.login: str = kwargs["login"]
        self.authorizedKeys: list[str] = kwargs["authorizedKeys"]
        self.sudoers: [str] = kwargs.get("sudoers", [])

class Config:
    def __init__(self, **kwargs):
        self.hostname: str = kwargs["hostname"]
        self.zerotierNetworkId: str = kwargs["zerotierNetworkId"]
        self.repositores = [AptRepo(**repo) for repo in kwargs["repositores"]]
        self.standalonePackages: list[str] = kwargs["standalonePackages"]
        self.users: list[UserConfig] = kwargs["users"]

class AptRepo:
    def __init__(self, **kwargs):
        self.name: str = kwargs["name"]
        self.file: str = kwargs["file"]
        self.source: [str] = kwargs.get("source", [])
        self.shellCommands: [str] = kwargs.get("shellCommands", [])
        self.packages: [str] = kwargs.get("packages", [])

deployerKeys = [
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINBjO1Y0Q3q8TTnupBWMEHp/G0yBZi0s6TvGvXepXFVt glen@fullfillment",
    "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3+BOkj22pM1TjJJx3K0KpcARuXBMz1JGCsFoyS+bhJmNA6TK7HFSQ7yDdes/dEhZP7fFRrMcji/lzNmSNg3p8kDyyFyCmCYjti7yaMG/OFhen6w8FzueI4Bm79AudkR3s2Z+fmgC2MzttXWvUt5cYqmmExitZ1Uy8SbU9Ehal9vJScOmurhVSshhfPgQIqc8duRy91Vdj9eW9vt39wmb3E2pOWUJTsm1VfciNXU10A+rd4ChJg4Kvc9xvj9M5PS6mUYbv7AgmrLvaG3i1yP4LQbRdzHL39JRapc5dHjDxWaU49PJUt5nj4EBVE3tIej/D/gFYaXWbAKjT56HkS/1Z raph@raph",
]

tulipConfig = Config(
    hostname = "tulip",
    zerotierNetworkId = "8056c2e21cb31b0c",
    repositores = [
        {
            "name": "fish shell",
            "file": "/etc/apt/sources.list.d/fish-shell-ubuntu-release-3-jammy.list",
            "source": ["ppa:fish-shell/release-3"]
        },{
            "name": "postgres",
            "file": "/etc/apt/sources.list.d/pgdg.list",
            "shellCommands": [
                """wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -""",
                """echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list""",
            ]
        },{
            "name": "caddy1",
            "packages": ["debian-keyring", "debian-archive-keyring", "apt-transport-https"],
            "file": "/etc/apt/sources.list.d/caddy-stable.list",
            "shellCommands": [
                "curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor > /usr/share/keyrings/caddy-stable-archive-keyring.gpg",
                "curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list"
            ]
        }
    ],
    standalonePackages = [
        "caddy",
        "supervisor",
        "rsync",
        "postgresql-13",
        "postgresql-client-13",
        "pgbackrest",
        "fish",
    ],
    users = [
        UserConfig(
            login = "dev",
            authorizedKeys = deployerKeys,
            sudoers = "dev ALL=(ALL) NOPASSWD: ALL"
        ),
        UserConfig(
            login = "postgres",
            authorizedKeys = deployerKeys,
        )

    ],
)

config = tulipConfig


aptUpdateNeeded = False

def setupRepos() -> None:
    for repo in config.repositores:
        installPackages(repo.packages)
        if not os.path.exists(repo.file):
            for source in repo.source:
                root.execAsUser(["apt-add-repository", "-y", source])
            for shellCommand in repo.shellCommandss:
                root.execAsUser(["apt-add-repository", "-y", source])
            aptUpdateNeeded = True
        else:
            print(f"repo {repo.name} already setup")    


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


def installPackages(packages: List[str]) -> None:
    if len(packages) == 0:
        pass
    elif not arePackagesInstalled(*packages):
        packagesL = list(packages)
        print("installing packages -- " + str(packagesL))
        root.execAsUser(["apt", "install", "-y"] + packagesL)
    else:
        print("packages already installed -- " + str(list(packages)))


def setupZerotier() -> None:
    if not os.path.exists("/usr/sbin/zerotier-cli"):
        root.execShell("curl -s https://install.zerotier.com | sudo bash")
        root.execAsUser(["zerotier-cli", "join", config.zerotierNetworkId])
    else:
        print("zerotier already installed")    


def configureCaddy() -> None:
    if not root.pathExists("/etc/caddy/apps-setup-complete"):
        root.copyFile(scriptDir / "Caddyfile", "/etc/caddy/Caddyfile")
        root.makeDirectories("/etc/caddy/apps/")
        root.execAsUser(["systemctl", "enable", "--now", "caddy"])
        root.writeFile("/etc/caddy/apps-setup-complete", "do nothing / noop marker file to show that apps have been setup")


def configureSupervisor() -> None:
    if not root.pathExists("/etc/supervisor/apps-setup-complete"):
        root.copyFile(scriptDir / "supervisord.conf", "/etc/supervisor/supervisord.conf")
        root.makeDirectories("/etc/supervisor/apps/")
        root.writeFile("/etc/supervisor/apps-setup-complete", "do nothing / noop marker file to show that apps have been setup")



def createSudoUser(userConfig: UserConfig) -> User:
    username = userConfig.login
    if not userExists(username):
        root.execAsUser(["adduser", "--disabled-password", "--gecos", "", username])
    if len(userConfig.sudoers) > 0:
        root.writeFile(f"/etc/sudoers.d/{username}", f"{username} ALL=(ALL) NOPASSWD: ALL")
    return User(username, userConfig.authorizedKeys)

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
        pkg = cache.get(package)
        return pkg is not None and pkg.installed is not None
    return all(isPackageInstalled(p) for p in packages)


def installEtcKeeper() -> None:
    global aptUpdateNeeded
    if not arePackagesInstalled("etckeeper"):
        aptUpdateNeeded = True
        aptUpdate()
        installPackages(["etckeeper"])


def createUser(userConfig: UserConfig) -> User:
    print(f"createAndOrSetupUser({userConfig.login})")
    user = createSudoUser(userConfig)
    return user


def fixAppsFolderPerms(devUser: User) -> None:
    """
    fixes perms for the apps folders
    needs to happen after the user is created
    """
    os.chown("/etc/caddy/apps", devUser.pw_uid, devUser.pw_gid)
    os.chown("/etc/supervisor/apps", devUser.pw_uid, devUser.pw_gid)


def createSymlink(target: Path, link: Path) -> bool:
    if not link.parent.exists():
        root.makeDirectories(link.parent)
    if not link.exists():
        if not target.exists():
            logWarning(f"target path does not exist @ {target}")
        else:
            print(f"creating symlink target={target}  link={link}")
            link.symlink_to(target)
            return True
    return False

def setupSystemSymlinks(devUser: User) -> None:

    javaExecPath = devUser.homePath(".nix-profile/bin/java").resolve()

    createSymlink(javaExecPath, Path("/usr/local/bin/java11"))
    createSymlink(javaExecPath, Path("/usr/local/bin/java"))
    createSymlink(devUser.homePath(".nix-profile/bin/runitor").resolve(), Path("/usr/local/bin/runitor"))
    createSymlink(devUser.homePath(".nix-profile/bin/a8-versions").resolve(), Path("/usr/local/bin/a8-versions"))


def logWarning(msg: str) -> None:
    print("WARNING !! " + msg)


root = User("root")

installEtcKeeper()
setHostname(config.hostname)

setupRepos()

aptUpdate()

installPackages(config.standalonePackages)

setupZerotier()

configureCaddy()
configureSupervisor()



users = [createUser(user) for user in config.users]

devUser = users[0]
devUser.installNix()

[user.standardConfig() for user in users]

fixAppsFolderPerms(devUser)

setupSystemSymlinks(devUser)

print("successfully completed")




