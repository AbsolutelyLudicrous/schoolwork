# Intro

## Thesis: The Filesystem Hierarchy Standard, the FHS, is good and should be conformed to, for the reason that physical storage media themselves are bad and failure prone.

## Required Background Knowledge

- Data

- Disks

- Disk Failure

- The Hierarchy

- Mounting

### Data:

Data is stuff on a computer.
Any form of information, any thing, on a computer.
Essays are data, your browser history is data, the core operating system is data.
Data can be read from or written to.
Reading is the process of taking data from someplace, writing is the process of putting new data someplace.

### Disks:

Computers store data.
This data can be stored on many forms of media, such as tape drives or floppy disks or more modern NAND cells.
The most common form is the hard disk drive, the HDD.
In an HDD, around five small disks spin at thousands of rounds per minute, and are read from or written to with a read/write head.
An HDD can be thought of as working like a gramophone.

### Disk Failure:

To read or write to a disk, the read/write head must make contact with the disk.
Modern disks can spin at around seven thousand RPM;
even high endurance disks, as are used at datacenters and are specialized for 24/7 read/write operations with no downtime, spin at "only" five thousand RPM.
Higher spin speeds mean that the read/write head will touch the disk at higher tangential speeds.

This puts quite a lot of wear and tear on a disk.
Disks have a lifespan, measured in read/writes.
Eventually, every disk will fail and all data on that disk will be lost.

There is no way to recover data from a failed disk.

### The Hierarchy:

Most data on a computer is stored in a filesystem.

Some data, such as boot entries or microcode is stored in other parts of the disk or the computer.
For the purposes of this essay, that other data does not exist.

All data on a computer is stored in a filesystem.
This filesystem is, with one exception, always hierarchical.
The filesystem, when drawn out on a sheet of paper, looks a bit like an upside-down tree.

It starts in one master directory, one master "folder", called `/`.
A literal `/`, usually pronounced as "slash" or "root".
Below `/` are other directories, usually `/bin/`,`/usr/`,`/lib/` and others.
Below those directories are yet more directories.

The layout of these directories is specified by the Filesystem Hierarchy Standard (The Linux Foundation).

### Mounting:

Disks can be mounted to a mountpoint.
Mounting is where the contents of one disk are treated as the mountpoint.
Continuing the tree analogy, mounting is like grafting another tree onto the primary tree.

When mounting a disk, the filesystem will lie and insist that there is still just one filesystem.
The whole filesystem maintains just the one tree, there are no seperate trees.

Mounting allows the filesystem to be spread across multiple disks.
For example, it is common to have `/home/` on a seperate partition or seperate disk.

### End informational preview

Conformation to the FHS is good, as it keeps the system simple, allows easy rescue of dead or dying systems, saves disk usage, and allows faster access to data.

Programs that run on your computer generally need to store data on the filesystem.
Common examples of such inter-session data include web browser history or a music library.
To operate on this data, the program needs to know where it is stored.
For this reason, the single "tree" hierarchy layout is better than multi-"tree" layouts.
This is because multi-tree layouts are finnicky and require special care to which tree is being written to or read from (Stack Overflow, Superuser).
In an FHS-compliant filesystem, temporary data can be relied on to be in `/var` on `/tmp`.
Systems which adhere to both the FHS and the XDG Base Directory Specification be relied on to have user-specific data in an XDG Directory (Bastian, Lortie, Poettering, the Freedesktop Group).
XDG Variables can be obtained by running `env | grep XDG` in a POSIX shell equipped with `coreutils` or equivalent.


