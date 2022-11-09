{ config, pkgs, lib, ... }:

let

  system = builtins.currentSystem;

  sources = import ./nix/sources.nix;

  nixpkgs = import sources.nixpkgs-unstable { inherit system; };

  a8-scripts = import sources.a8-scripts { inherit system nixpkgs; };

  # runitor = 
  #   pkgs.buildGoModule rec {
  #     pname = "runitor";
  #     version = "0.8.0";
  #     vendorSha256 = null;
  #     src = pkgs.fetchurl {
  #       url = "https://github.com/bdd/runitor/archive/refs/tags/v0.8.0.tar.gz";
  #       sha256 = "71489ba9b0103f16080495ea9671dd86638c338faf5cb0491f93f5d5128006c3";
  #     };
  #   };

in
{

  programs.home-manager.enable = true;

  # The home-manager manual is at:
  #
  #   https://rycee.gitlab.io/home-manager/release-notes.html
  #
  # Configuration options are documented at:
  #
  #   https://rycee.gitlab.io/home-manager/options.html

  # Home Manager needs a bit of information about you and the
  # paths it should manage.
  #
  # You need to change these to match your username and home directory
  # path:


  home.username = builtins.getEnv "USER";
  home.homeDirectory = builtins.getEnv "HOME";

  # If you use non-standard XDG locations, set these options to the
  # appropriate paths:
  #
  # xdg.cacheHome
  # xdg.configHome
  # xdg.dataHome

  # This value determines the Home Manager release that your
  # configuration is compatible with. This helps avoid breakage
  # when a new Home Manager release introduces backwards
  # incompatible changes.
  #
  # You can update Home Manager without changing this value. See
  # the Home Manager release notes for a list of state version
  # changes in each release.
  home.stateVersion = "22.11";

  programs.direnv.enable = true;
  programs.direnv.nix-direnv.enable = true;

  # optional for nix flakes support in home-manager 21.11, not required in home-manager unstable or 22.05
  # programs.direnv.nix-direnv.enableFlakes = true;

  programs.bash.enable = true;
  programs.zsh.enable = true;

  programs.fish = {
    enable = true;

    plugins = [
      {
        name = "bass";
        src = pkgs.fetchFromGitHub {
          owner = "edc";
          repo = "bass";
          rev = "50eba266b0d8a952c7230fca1114cbc9fbbdfbd4";
          sha256 = "0ppmajynpb9l58xbrcnbp41b66g7p0c9l2nlsvyjwk6d16g4p4gy";
        };
      }

      {
        name = "foreign-env";
        src = pkgs.fetchFromGitHub {
          owner = "oh-my-fish";
          repo = "plugin-foreign-env";
          rev = "dddd9213272a0ab848d474d0cbde12ad034e65bc";
          sha256 = "00xqlyl3lffc5l0viin1nyp819wf81fncqyz87jx8ljjdhilmgbs";
        };
      }
    ];
  };

  home.packages = [
    a8-scripts.a8-scripts
    nixpkgs.htop
    nixpkgs.jdk11
    nixpkgs.fortune
    # runitor

#    my-ammonite
#    pkgs.activemq
    pkgs.awscli
    pkgs.bottom
    pkgs.curl
#   pkgs.diffoscope    
    pkgs.direnv
    pkgs.drone-cli
    pkgs.exa  
    pkgs.fish
    pkgs.git
    pkgs.git-crypt
    pkgs.gnupg
#    pkgs.haxe_4_0
    pkgs.htop
    pkgs.httping
    pkgs.iftop
    # this classes with nettools
    # pkgs.inetutils
    pkgs.jq
#    my-java
    # pkgs.ipython
    pkgs.lf
    pkgs.micro
    pkgs.mtr
    pkgs.nano
    pkgs.ncdu
    pkgs.ncftp
    pkgs.nettools
    pkgs.niv
    pkgs.nnn
    pkgs.pgcli
    pkgs.powerline-go
    pkgs.pstree
    # my-python3
    pkgs.ripgrep
    pkgs.rsync
    pkgs.s3cmd
    pkgs.s4cmd
    pkgs.mypy
    # my-scala
#    my-sbt
    pkgs.silver-searcher
    pkgs.tea
    pkgs.tmux
    pkgs.websocat
    pkgs.wget
    pkgs.xz
    pkgs.zsh
#    my-scala
#    pkgs.byobu
    # pkgs.tcping
    pkgs.cached-nix-shell
  ];

}
