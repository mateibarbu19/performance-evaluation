# Rotational delay - IOPS calculations

$$\overline{IOPS} = {1 \over \overline{latency} + \overline{seek}}$$

Calculate the Rotational Delay - RD for a 5400 RPM drive:

- Divide 5400 RPM by 60 seconds: ${5400 \over 60} = 90$ RPS
- Convert 1 of 90 to decimal: ${1 \over 90} = 0.0(1)$ seconds per Rotation
- Multiply the seconds per rotation by 1000 milliseconds ($11.(1)$ ms per
  rotation).
- Divide the total in half (RD is considered half a revolution around a disk):
  ${11.(1) \over 2} = 5.(5)$ ms
- Add an average of $3$ ms for seek time: $8.(5)$ ms
- Add $2$ ms for latency (internal transfer): $10.(5)$ ms
- Divide $1000$ ms by $10.(5)$ ms per I/O: ${1000 \over 10.(5)} = 
  {1000 \cdot 9 \over 95} = 94.736842105$ IOPS

# `iostat` & `iotop`

## Monitoring the behavior with `iostat`

Prerequisite:

```bash
sudo sh -c "sync && echo 3 > /proc/sys/vm/drop_caches"
```

[![`iostat`](https://asciinema.org/a/eqNsmkDUaauPjAdeMTj5bZd0n.svg)](https://asciinema.org/a/eqNsmkDUaauPjAdeMTj5bZd0n)

I selected the last two statistic:

```bash
Device  r/s     rkB/s           w/s     wkB/s
nvme0n1 969,00  496128,00       970,00  495624,00


Device  r/s     rkB/s           w/s     wkB/s
nvme0n1 358,00  183296,00       2001,00 1023044,00
```

$$IOPS_{read_1} = {496128 \over 969} = 512$$
$$IOPS_{read_2} = {183296 \over 358} = 512$$

$$IOPS_{write_1} = {495624 \over 970} = 510.95$$
$$IOPS_{write_2} = {1023044 \over 2001} = 511,26$$

Compared to what a [external benchmark](https://score.nero.com/ssd-hdd-benchmark/WDC_PC_SN520_SDAPMUW-512G-1101) tested, I believe that the performance
was overall good, and some tests could increase the block size in `dd` for
further investigation.

> 4K Random read/write812/743 MB/s

## Monitoring the behavior with `iotop`

[![`iotop`](https://asciinema.org/a/aWuJnTsz53zidRxuy38YmrXIW.svg)](https://asciinema.org/a/aWuJnTsz53zidRxuy38YmrXIW)

Use this to kill from another window:

```bash
kill -SIGKILL "$(pgrep ^dummy)"
```

As we can see, since the script reads from `/dev/zero/`, aka. a driver, and
writes to a physical file, only write speed is stressed.

# RAM disk

## Create a RAM disk

```bash
$ sudo mkdir /mnt/ramdisk
$ sudo mount -t tmpfs -o size=1G ext4 /mnt/ramdisk
$ sudo df -Th
Filesystem     Type      Size  Used Avail Use% Mounted on
udev           devtmpfs  7,7G     0  7,7G   0% /dev
tmpfs          tmpfs     1,6G  1,6M  1,6G   1% /run
/dev/nvme0n1p2 ext4      196G  105G   82G  57% /
tmpfs          tmpfs     7,8G   93M  7,7G   2% /dev/shm
tmpfs          tmpfs     5,0M  4,0K  5,0M   1% /run/lock
/dev/nvme0n1p3 ext4      196G   72G  115G  39% /media/matei/Date
/dev/nvme0n1p1 vfat     1022M   32M  991M   4% /boot/efi
tmpfs          tmpfs     1,6G  128K  1,6G   1% /run/user/1000
ext4           tmpfs     1,0G     0  1,0G   0% /mnt/ramdisk
```

## Pipe View & RAM Disk

**Disclaimer:** Piped view didn't work.

```bash
$ dd if=/dev/urandom of=/mnt/ramdisk/rand  bs=2048 count=$((512 * 1024 * 1024 / 2048))
262144+0 records in
262144+0 records out
536870912 bytes (537 MB, 512 MiB) copied, 1,7768 s, 302 MB/s
$ dd if=/dev/urandom of=/home/matei/rand  bs=2048 count=$((512 * 1024 * 1024 / 2048))
262144+0 records in
262144+0 records out
536870912 bytes (537 MB, 512 MiB) copied, 2,63085 s, 204 MB/s
```

Given the higher throughput of the writes to `tmpfs`, I would use it for small
volatile data storage, like `redis`.

# `perf` & fuzzing

## Fuzzing with AFL

```bash
$ git clone https://github.com/google/AFL  
Cloning into 'AFL'...
remote: Enumerating objects: 531, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 531 (delta 0), reused 2 (delta 0), pack-reused 527
Receiving objects: 100% (531/531), 997.50 KiB | 2.81 MiB/s, done.
Resolving deltas: 100% (193/193), done.
$ pushd AFL
~/Public/AFL ~/Public
/AFL$ make -j $(nproc)
[*] Checking for the ability to compile x86 code...
[+] Everything seems to be working, ready to compile.
...
AFL$ export PATH="${PATH}:$(pwd)"
AFL$ export AFL_PATH="$(pwd)"
AFL$ popd
~/Public
$ afl-fuzz --help
afl-fuzz 2.57b by <lcamtuf@google.com>
...
$ afl-gcc --version
afl-cc 2.57b by <lcamtuf@google.com>
...
$ git clone https://github.com/fuzzstati0n/fuzzgoat.git
Cloning into 'fuzzgoat'...
remote: Enumerating objects: 127, done.
remote: Total 127 (delta 0), reused 0 (delta 0), pack-reused 127
Receiving objects: 100% (127/127), 26.40 KiB | 614.00 KiB/s, done.
Resolving deltas: 100% (61/61), done.
$ pushd fuzzgoat
~/Public/fuzzgoat ~/Public
/fuzzgoat$ CC=afl-gcc make
afl-gcc -o fuzzgoat -I. main.c fuzzgoat.c -lm
afl-cc 2.57b by <lcamtuf@google.com>
afl-as 2.57b by <lcamtuf@google.com>
[+] Instrumented 74 locations (64-bit, non-hardened mode, ratio 100%).
afl-as 2.57b by <lcamtuf@google.com>
[+] Instrumented 369 locations (64-bit, non-hardened mode, ratio 100%).
afl-gcc -fsanitize=address -o fuzzgoat_ASAN -I. main.c fuzzgoat.c -lm
afl-cc 2.57b by <lcamtuf@google.com>
afl-as 2.57b by <lcamtuf@google.com>
[+] Instrumented 46 locations (64-bit, ASAN/MSAN mode, ratio 33%).
afl-as 2.57b by <lcamtuf@google.com>
[+] Instrumented 330 locations (64-bit, ASAN/MSAN mode, ratio 33%).
/fuzzgoat$ popd
~/Public
$ afl-fuzz -i fuzzgoat/in -o afl_output -- ./fuzzgoat/fuzzgoat @@
afl-fuzz 2.57b by <lcamtuf@google.com>
[+] You have 8 CPU cores and 1 runnable tasks (utilization: 12%).
[+] Try parallel jobs - see docs/parallel_fuzzing.txt.
[*] Checking CPU core loadout...
[+] Found a free CPU core, binding to #0.
[*] Checking core_pattern...
[*] Checking CPU scaling governor...

[-] Whoops, your system uses on-demand CPU frequency scaling, adjusted
    between 390 and 3906 MHz. Unfortunately, the scaling algorithm in the
    kernel is imperfect and can miss the short-lived processes spawned by
    afl-fuzz. To keep things moving, run these commands as root:

    cd /sys/devices/system/cpu
    echo performance | tee cpu*/cpufreq/scaling_governor
...
$ cd /sys/devices/system/cpu/
$ echo performance | sudo tee cpu*/cpufreq/scaling_governor
performance
$ cd -
$ sudo su
$ # export PATH again...
$ afl-fuzz -i fuzzgoat/in -o afl_output -- ./fuzzgoat/fuzzgoat @@
```

```python

                      american fuzzy lop 2.57b (fuzzgoat)

   process timing                                         overall results        
         run time : 0 days, 0 hrs, 37 min, 15 sec                cycles done : 10        
    last new path : 0 days, 0 hrs, 2 min, 20 sec                 total paths : 427       
  last uniq crash : 0 days, 0 hrs, 32 min, 46 sec               uniq crashes : 22        
   last uniq hang : none seen yet                                 uniq hangs : 0         
   cycle progress                        map coverage                            
   now processing : 392* (91.80%)              map density : 0.16% / 0.80%               
  paths timed out : 0 (0.00%)               count coverage : 3.70 bits/tuple             
   stage progress                        findings in depth                        
   now trying : havoc                       favored paths : 94 (22.01%)                  
  stage execs : 3960/12.3k (32.23%)          new edges on : 126 (29.51%)                 
  total execs : 6.36M                       total crashes : 2234 (22 unique)             
   exec speed : 2956/sec                     total tmouts : 2 (1 unique)                 
   fuzzing strategy yields                                 path geometry           
    bit flips : 27/220k, 8/220k, 6/219k                         levels : 16              
   byte flips : 0/27.6k, 0/22.0k, 1/21.8k                      pending : 66              
  arithmetics : 53/1.23M, 0/139k, 0/2511                      pend fav : 0               
   known ints : 4/114k, 0/605k, 0/958k                       own finds : 426             
   dictionary : 0/0, 0/0, 0/0                                 imported : n/a             
        havoc : 349/2.55M, 0/0                               stability : 100.00%         
         trim : 79.62%/12.5k, 19.20%                                                 
                                                             [cpu000: 39%]

+++ Testing aborted by user +++
```

## 

As root:

```bash
$ perf record -e cycles -c 1000 -g --all-user \
    afl-fuzz -i fuzzgoat/in -o afl_output -- ./fuzzgoat/fuzzgoat @@
$ perf script -i perf.data
afl-fuzz 18517 10832.011321:       1000 cycles: 
            7fa2992f9090 _dl_start+0x2b0 (/usr/lib/x86_64-linux-gnu/ld-2.31.so)

afl-fuzz 18517 10832.011326:       1000 cycles: 
            7fa2992f9de0 dl_main+0x900 (/usr/lib/x86_64-linux-gnu/ld-2.31.so)

afl-fuzz 18517 10832.011328:       1000 cycles: 
        ffffffff88c00af0 [unknown] ([unknown])
            7fa2992f9de0 dl_main+0x900 (/usr/lib/x86_64-linux-gnu/ld-2.31.so)

afl-fuzz 18517 10832.011335:       1000 cycles: 
            7fa2992f9e1c dl_main+0x93c (/usr/lib/x86_64-linux-gnu/ld-2.31.so)
            7fa2992f9098 _dl_start+0x2b8 (/usr/lib/x86_64-linux-gnu/ld-2.31.so)
$ perf report -i perf.data
+   38,90%    38,38%  fuzzgoat  libc-2.31.so      [.] __strncasecmp_l_sse42
+   38,26%     0,00%  fuzzgoat  [unknown]         [.] 0x756e696c2d34365f
+   38,26%     0,00%  fuzzgoat  [unknown]         [.] 0x00007f17a8af7000
+   13,72%    13,69%  afl-fuzz  afl-fuzz          [.] run_target
+   12,68%    12,67%  afl-fuzz  afl-fuzz          [.] save_if_interesting
+   12,45%     0,00%  afl-fuzz  [unknown]         [.] 0000000000000000
+    7,41%     7,41%  fuzzgoat  [unknown]         [k] 0xffffffff88c00af0
+    7,35%     0,00%  afl-fuzz  [unknown]         [.] 0x677a7a75662f7461
+    7,35%     0,00%  afl-fuzz  [unknown]         [.] 0x000056348ff2b038
+    5,48%     0,00%  afl-fuzz  libc-2.31.so      [.] 0x00007fa29924a6fa
+    5,45%     5,45%  afl-fuzz  libc-2.31.so      [.] 0x00000000001616fa
+    4,28%     4,27%  afl-fuzz  afl-fuzz          [.] fuzz_one
+    3,97%     0,00%  fuzzgoat  [unknown]         [.] 0x5541d68949564100
+    3,10%     3,09%  afl-fuzz  libc-2.31.so      [.] __vfwscanf_internal
+    2,69%     1,49%  fuzzgoat  libc-2.31.so      [.] __posix_spawn_file_actions_adddup2
+    1,63%     1,26%  fuzzgoat  ld-2.31.so        [.] remove_slotinfo
+    1,60%     0,00%  fuzzgoat  [unknown]         [.] 0000000000000000
+    1,52%     0,94%  fuzzgoat  libc-2.31.so      [.] ____wcstod_l_internal
+    1,36%     0,58%  fuzzgoat  libc-2.31.so      [.] getnetbyname_r@@GLIBC_2.2.5
+    0,93%     0,44%  fuzzgoat  libc-2.31.so      [.] __strncat_sse2_unaligned
+    0,81%     0,81%  afl-fuzz  libc-2.31.so      [.] ____wcstod_l_internal
     0,77%     0,35%  fuzzgoat  fuzzgoat          [.] __afl_store
+    0,76%     0,76%  afl-fuzz  afl-fuzz          [.] UR
+    0,74%     0,17%  fuzzgoat  libc-2.31.so      [.] __spawn_valid_fd
     0,54%     0,48%  fuzzgoat  fuzzgoat          [.] __afl_fork_wait_loop
     0,52%     0,47%  afl-fuzz  libc-2.31.so      [.] getnetbyaddr_r@@GLIBC_2.2.5
+    0,52%     0,00%  afl-fuzz  [unknown]         [.] 0x5f7275632e2f7475
     0,51%     0,05%  fuzzgoat  ld-2.31.so        [.] _dl_start
```

# Feedback

Note I am using Bucharest local configuration.

```bash
$ firefox https://forms.gle/LWBWYsMiJq8FsYdN9
$ date | md5sum
427cacdab2d444456e4914e98cd87fd9  -
```