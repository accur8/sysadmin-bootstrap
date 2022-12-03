#!/usr/bin/env bash

cd "$(dirname "$0")"

export PATH=$PATH:/nix/var/nix/profiles/default/bin/

nix-shell --run "home-manager switch -b backup"
