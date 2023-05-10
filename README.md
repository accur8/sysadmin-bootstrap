
This is a minimal script to take a scratch intall of ubuntu
and get things bootstrapped on it so our standard tooling
can then take over from there.

bootstrapped items are

  * nix
  * zerotier
  * hostname
  * caddy 
  * etckeeper
  * users created
  * for each user 
    * minimal ssh keys setup (so the Raph/Glen can get in with a8-versions to do the rest)
    * chezmoi with accur8 dotfiles repo

Our standard tooling is nix, homemanager, chezmoi and a8-versions.



