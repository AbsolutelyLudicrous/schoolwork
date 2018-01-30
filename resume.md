## Danne's Resume

#### (Or, what the heck do they spend all their time in their room doing, anyways?)

---

**Systems**: What I use to do my computing

Daily driver:
[Solus](solus-project.com/), a GNU/Linux distribution designed for average home use.
Solus is fast (it cold-boots in eight seconds!), rolling-release, and easy to use.
It's the OS that first got me into GNU/Linux and further Unixes.

Servers:
[FreeBSD](https://www.freebsd.org/), the most widely used BSD.
FreeBSD is awesome for data storage and virtualization.
Native ZFS support allows me to easily manage the collection of flash drives and USB hard drives I call a NAS,
and Jails are awesome for when I need to spin up a GNU/Linux distribution for some weird (usually Docker related) reason.
Also GEOM is the best thing since sliced bread, as it prevents me from needing a live USB for partition management;
I can just resize mounted partitions without any negative consequences and that is too useful for me to not use.
Even further on the data storage aspect, geli encryption is much easier to use than dm-crypt.

Experimental:
[Artix](artixlinux.org/), a GNU/Linux distribution forked from Arch and redesigned to use OpenRC instead of systemd for init.
It's Arch, without [the many issues that systemd has](https://suckless.org/sucks/systemd).
systemd is absurd and bloated, and just does stupid things, too many things (why does my init also handle DNS?), and frequently too many stupid things.
Arch is a highly-respected distribution designed to be minimal out of the box, with plenty of room for customization.
Why not use both?

Other:
[Debian](https://www.debian.org/), in a FreeBSD Jail, for running programs that don't like to cooperate with FreeBSD.
[RISC OS Open](https://www.riscosopen.org/content/), on an RPiturned-MP3-player, because I like making die-hard Unix nerds wonder if I'm running [an operating system from the eighties](https://en.wikipedia.org/wiki/RISC_OS).
(Sometimes!)[OpenIndiana](https://www.openindiana.org/), because enough people told me that "Solus" sounds like "Solaris" that I figured I had to give a Solaris derivative a try.

---

**Services**: What I put these poor machines through

 - `ssh` on all of them.

 - `rsync`, one machine pulls the `~/.config`s of every other system to ensure that my experience remains the same across all systems.

 - Weekly `/(usr/)home/` partition backups on the NAS, stored tarred and encrypted.

 - Gitea, a self-hosted Git server.

 - NFS: Network File System, used for sharing `/(usr/)home/` across multiple systems.

---

**Languages**: I actually still program sometimes

Supposedly, [I have experience with four useful programming languages and Haskell](https://github.com/AbsolutelyLudicrous/schoolwork/tree/master/workspaces<Paste>).
If POSIX Shell counts as a language, then I have experience with five useful languages and Haskell.

For some reason I'm allowed to teach other people how to program in Python, and do so every Monday.
The thought of people following my coding practices scares me, but that's their problem.

---

**Software**: I have *very* strong opinions on why the software you use is bad and why the software I use is better.

 - NeoViM, it's ViM except modern and with half-decent plugins.

 - ZSH, it's cooler than your shell.

 - Git, it's the most featureful version control system.

 - Eclipse, it's the best Java IDE which doesn't have any form of corporate influence.
