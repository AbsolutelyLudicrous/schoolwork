Danne

Ms. Street

English III

20180205

# Title!

Data is stuff on a computer.
Any form of information, any thing, on a computer.
Essays are data, browser history is data, the core operating system is data.
Data can be read from or written to.
Reading is the process of taking data from someplace, writing is the process of putting new data someplace.


Computers store data.
This data can be stored on many forms of media, such as tape drives or floppy disks or more modern NAND cells.
The most common form is the hard disk drive, the HDD.
In an HDD, around five small disks spin at thousands of rounds per minute, and are read from or written to with a read/write head.
An HDD can be thought of as working like a gramophone.

To read or write to a disk, the read/write head must make contact with the disk.
Modern disks can spin at around seven thousand RPM;
even high endurance disks, as are used at datacenters and are specialized for 24/7 read/write operations with no downtime, spin at "only" five thousand RPM.
Higher spin speeds mean that the read/write head will touch the disk at higher tangential speeds.

This puts quite a lot of wear and tear on a disk.
Disks have a lifespan, measured in read/writes.
Eventually, every disk will fail and all data on that disk will be lost.
There is no way to recover data from a failed disk.

Most data on a computer is stored in a filesystem.
Some data, such as boot entries or microcode is stored in other parts of the disk or the computer.
For the purposes of this essay, that other data does not exist.

All data on a computer is stored in a filesystem.
This filesystem is, with one exception, always hierarchical.
The filesystem, when drawn out on a sheet of paper, looks a bit like an upside-down tree.

It starts in one master directory, one master "folder", called "/".
A literal "/", usually pronounced as "slash" or "root".
Below "/" are other directories, usually "/bin/","/usr/","/lib/" and others.
Below those directories are yet more directories.

The layout of these directories is specified by the Filesystem Hierarchy Standard (The Linux Foundation).

Disks can be mounted to a mountpoint.
Mounting is where the contents of one disk are treated as the mountpoint.
Continuing the tree analogy, mounting is like grafting another tree onto the primary tree.
When mounting a disk, the filesystem will lie and insist that there is still just one filesystem.
The whole filesystem maintains just the one tree, there are no seperate trees.
Mounting allows the filesystem to be spread across multiple disks.
For example, it is common to have "/home/" on a seperate partition or seperate disk.

Computers should have their filesystems layed out logically.
The common standard is the called The Filesystem Hierarchy.
This standard may vary, and some systems may use a variant of the FHS, but the concepts of the FHS remain consistent across all Unix-like operating systems.
The Filesystem Hierarchy Standard, the FHS, is good and should be conformed to, for the reason that physical storage media themselves are bad and failure prone.
Conformation to the FHS is good, as it keeps the system simple, allows easy rescue of dead or dying systems, saves disk usage, and allows faster access to data.

Programs that run on a computer generally need to store data on the filesystem.
Common examples of such inter-session data include web browser history or a music library.
To operate on this data, the program needs to know where it is stored.
For this reason, the single "tree" hierarchy layout is better than multi-"tree" layouts.
This is because, as evidenced by the concerning number of questions about how to discover which partition something is on, multi-tree layouts are finnicky and require special care to which tree is being written to or read from (Stack Overflow, Superuser).
In an FHS-compliant filesystem, temporary data can be relied on to be in "/var/" or "/tmp/".
Systems which adhere to both the FHS and the XDG Base Directory Specification be relied on to have user-specific data in an XDG Directory as specified by the Freedesktop Group (The Freedesktop Group).
XDG Variables can be obtained by running "env | grep XDG" in a POSIX shell equipped with "GNU coreutils" or equivalent.
No such assurance of location exists on a non-FHS system.
On a non-FHS compliant system, a program must take the time to search the filesystem for where its files are, or ask the user.
This slows down loading and interrupts workflow.

Programs on an FHS compliant system are typically located in "/bin/", "/usr/bin/", "/sbin/", or "/usr/sbin/".
"bin" is short for "binary", a term for a compiled machine-executable program, opposed to the raw source code of a program.
"sbin" is similar, it is short for "superuser binary", binarys located in "sbin" are meant to only be excuted by root, the superuser, an all-powerful user account for the purpose of performing important systems administration tasks.
The reason that "bin" and "sbin" are seemingly duplicated is because, traditionally, "/usr/" might be mounted from a seperate disk, and "/usr/bin/" is a subdirectory of "/usr/".
If the "/usr/" disk were to fail, only non-critical binarys are lost.
"/bin/" and "/sbin/" are reserved for system-critical binarys, programs which can not be lost without undergoing catastrophic system failure.
This makes sense, disks fail all the time.
The failure of a single disk should not bring down an entire system.
Compare to a non-FHS compliant system, such as Windows.
Windows stores all of its programs on C:\, even system-critical ones.
If the C: disk on a Windows system were to fail, the system would be unrecoverable.
Obviously, being able to recover from hardware failure is generally beneficial.
Hardware failure is inevitable, but can be delayed through mounting.

The FHS extends the lifespan of disks.
Read/writes put wear on disks, an easy way to extend the lifespan of a disk is to perform fewer read/writes on it.
Through mounting, a system can have its files spread across multiple disks.
A common arrangement on home computers is to have one root filesystem containing all operating system level files, and one filesystem containing the "/(usr/)home/" directory.
Such a setup ensures that user data is kept far away from system data.
An enterprise system may have one filesystem mounted at each FHS-defined directory, such as seperate filesystems for "/usr/" and "/etc/".
This setup can keep a system functional well after multiple disks have failed, and is further augmented by solutions such as RAID or disk pooling.
Critical mountpoints can even be mounted read-only, which prevents the system from modifying the contents at all.
Non-FHS compliant systems chew through disks and need frequent replacement, making them incredibly unsuited for use in a production environment.

Detractors of the FHS may claim that it's pointless to use when RAID, Redundant Array of Independent Disks, and JBOD, Just a Bunch of Disks, exist.
RAID and JBOD have huge limitations, which vary depending on the scheme used.
RAID 0, where data is "striped" across all disks, is prone to data loss; the loss of a single disk in RAID 0 loses all data.
RAID 1, where data is "mirrored" between disks, is expensive, can not be incrementally upgraded, and limits storage to the size of the smallest disk in the RAID.
RAIDs 2 through 6 have the same problems as RAID 1, but require even more disks.
JBOD has the same problems as RAID 0, except it requires slow software-level handling opposed to RAID's hardware-level handling.
While RAID and JBOD are by no means pointless, they simply aren't enough of a reason to abandon the FHS.

Indirectly, the FHS can speed up access to data.
This is done again through mounting.
Because it is possible to mount multiple disks on one filesystem, and disk read/write speed is limited by the rotation speed of the disk and the position of the read/write head, data access can be sped up by performing concurrent read/writes across multiple physical disks.
Data access can be sped up even further by utilizing a RAID or JBOD scheme, or using a filesystem-level disk pooling scheme such as offered by btrfs or ZFS.
On a non-FHS compliant system, data can be read from or written to at the same speeds, but can take much longer to find (Stack Overflow).
Precious time must be wasted finding the correct filesystem to operate on, which has the side effect of slowing data access.

FHS compliancy is valuable, and a huge benefit to any filesystem.
Compliancy hardens a system against unavoidable hardware failure and lowers the frequency of hardware failure.
Lack of compliancy makes it hard to find data, which in turn slows data access.
The Filesystem Hierarchy Standard should be conformed to.
