# Task 01 - `vmstat`

## A - Monitoring stress

[![asciicast](https://asciinema.org/a/XVqCk7lCqxo5LrxPEOaDCKWSh.svg)](https://asciinema.org/a/XVqCk7lCqxo5LrxPEOaDCKWSh)

## B - How does it work?

```bash
$ strace vmstat 2>&1 | grep --color '/proc'
openat(AT_FDCWD, "/proc/self/auxv", O_RDONLY) = 3
openat(AT_FDCWD, "/proc/sys/kernel/osrelease", O_RDONLY) = 3
openat(AT_FDCWD, "/proc/self/auxv", O_RDONLY) = 3
openat(AT_FDCWD, "/usr/share/locale/en_US.UTF-8/LC_MESSAGES/procps-ng.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/share/locale/en_US.utf8/LC_MESSAGES/procps-ng.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/share/locale/en_US/LC_MESSAGES/procps-ng.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/share/locale/en.UTF-8/LC_MESSAGES/procps-ng.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/share/locale/en.utf8/LC_MESSAGES/procps-ng.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/share/locale/en/LC_MESSAGES/procps-ng.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/proc/sys/kernel/osrelease", O_RDONLY) = 3
openat(AT_FDCWD, "/proc/meminfo", O_RDONLY) = 3
openat(AT_FDCWD, "/proc/stat", O_RDONLY) = 4
openat(AT_FDCWD, "/proc/vmstat", O_RDONLY) = 5
```

## C - USO flashbacks

```bash
$ sudo vmstat -d | tail -n +3
nvme0n1  64121  47316 5648488   16469  30561  29258 1671410   78920      0     66
```

# Task 03 - Zip with compression levels

## A - Measurements

```bash
$ TIMEFORMAT=%R; for i in {0..9}; do echo $i; time zip -$i -q archive.zip *.BMP big.txt; du archive.zip; done
0
0,071
11908   archive.zip
1
0,220
5628    archive.zip
2
0,244
5440    archive.zip
3
0,336
5276    archive.zip
4
0,316
5184    archive.zip
5
0,476
5068    archive.zip
6
0,636
5012    archive.zip
7
0,787
5000    archive.zip
8
0,989
4992    archive.zip
9
1,152
4992    archive.zip
```

# B - Plot