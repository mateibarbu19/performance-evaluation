# Task 01 - `Memory usage`

- `do_allocate()`: reserves the minimum amount of virtual pages for a array,
  before using a cell in it
- `do_append()`: reserves a memory page each time it needs it, and uses it
  immediately

**Disclaimer**: I have 16GB of RAM and no swap.

[![Experiment 1](https://asciinema.org/a/K0QW2zkZVCeXW9VuTce6wp9FD.svg)](
  https://asciinema.org/a/K0QW2zkZVCeXW9VuTce6wp9FD)

For the first experiment, as it can be seen, the free memory decreases, and the
number of interrupts and context switches increases. The increase of context
switches are causes by the requests made to the kernel for pages, and the
interrupts are generated when a reserved page is accessed, which causes a fault.

[![Experiment 2](https://asciinema.org/a/c9H1JBnFjTQkguzszKnuweMOS.svg)](
  https://asciinema.org/a/c9H1JBnFjTQkguzszKnuweMOS)

The only difference from the first experiment is the amount of free memory has
dropped.

[![Experiment 3](https://asciinema.org/a/iYRKO7cRnv6yb0slscNw3tXwU.svg)](
  https://asciinema.org/a/iYRKO7cRnv6yb0slscNw3tXwU)

For the third experiment we can see that the free memory plummets right after
each call is made, and shoots back up when it's done. Buffer and cache memory
follow a similar pattern but no as abrupt. The same reasoning for the interrupts
and context switching applies.

Experiment 4 is the same.

`do_append` should be rewritten like this:

```python
def do_append(size):
  result = [None for i in range(size)]
  for i in range(size):
    message= "some unique object %d" % ( i, ) * 1000
    result[i] = message
    time.sleep(0.0001)
  return result
```

# Task 02 - Swap space

## A - Swap File

```bash
$ sudo swapoff -a
$ sudo dd if=/dev/zero of=/swapfile bs=1024 count=$((4 * 1024 * 1024))
4194304+0 records in
4194304+0 records out
4294967296 bytes (4,3 GB, 4,0 GiB) copied, 15,128 s, 284 MB/s
$ sudo chmod 600 /swapfile
$ sudo mkswap /swapfile
Setting up swapspace version 1, size = 4 GiB (4294963200 bytes)
no label, UUID=068e0975-f6e4-4ab4-9d30-98eef7e91b84
$ sudo swapon /swapfile
$ swapon --show
NAME      TYPE SIZE USED PRIO
/swapfile file   4G   0B   -2
```

## B - Does it work?

I changed the size form the first experiment and reran the experiment.

```bash
if __name__ == '__main__':
  size = 10000000
```

```bash
$ python3 ex1.py & vmstat 1 | awk '{ print $3, $4 }' &
[1] 37251
[2] 37253
$ ---swap-- -----io----
swpd free
256 432884
256 267968
256 223296
256 223532
256 219568
256 215904
256 187652
512 186396
1024 168256
1024 171764
...
1024 176520
1024 178176
1024 168956
11520 168484
14336 172488
27904 183248
43008 229304
53504 201188
58112 196052
79872 179508
82176 180544
91648 170784
108544 172108
126976 169840
144384 172068
158976 169900
51148 176148
0 171276
0 173180
0 170124
```

This is however a good run. On another when only when RAM usage surpasses
`$(cat /proc/sys/vm/swappiness)`, we see the swap kick in.

```bash
$ sudo swapoff -a
$ sudo dd if=/dev/zero of=/swapfile1 bs=1024 count=$((4 * 1024 * 1024))
4194304+0 records in
4194304+0 records out
4294967296 bytes (4,3 GB, 4,0 GiB) copied, 15,128 s, 284 MB/s
$ sudo dd if=/dev/zero of=/swapfile2 bs=1024 count=$((4 * 1024 * 1024))
4194304+0 records in
4194304+0 records out
4294967296 bytes (4,3 GB, 4,0 GiB) copied, 15,128 s, 284 MB/s
$ sudo chmod 600 /swapfile1
$ sudo chmod 600 /swapfile2
$ sudo mkswap /swapfile1
Setting up swapspace version 1, size = 4 GiB (4294963200 bytes)
no label, UUID=068e0975-f6e4-4ab4-9d30-98eef7e91b84
$ sudo mkswap /swapfile2
Setting up swapspace version 1, size = 4 GiB (4294963200 bytes)
no label, UUID=14eaffc5-dea9-4682-99b2-815e83db1a54
$ sudo mkswap /swapfile2
$ sudo swapon -p 10 /swapfile1
$ sudo swapon -p 20 /swapfile1
$ swapon --show
NAME       TYPE SIZE USED PRIO
/swapfile1 file   4G   0B   10
/swapfile2 file   4G   0B   20
```

The advantages of having a swapfile instead of a partition is that it reduces
SSD lifetime shortage, since there are more logical sectors to be worn out,
but if the internal SSD mechanism doesn't manage this well, this could lead
to chaotic usage. A swapfile can be easily increased or decreased in size
and removes the need to create a extended partition for a MBR boot system
with dual-boot.

However a boot partition is setup easily within a installer like Calamares
and is persistent between reinstalls.

# Task 03 - Kernel Samepage Merging

## Task A - Check kernel support & enable ksmd

```bash
$ grep CONFIG_KSM /boot/config-$(uname -r)
CONFIG_KSM=y
# echo "1" > /sys/kernel/mm/ksm/run
# echo "1000" > /sys/kernel/mm/ksm/pages_to_scan 
# echo "1000000" > /sys/kernel/mm/ksm/max_page_sharing 
```

## Task B - Watch the magic happen

[![KSM experiment](https://asciinema.org/a/EUoF8M2pGp8zATliJ4u1yM0fa.svg)](https://asciinema.org/a/EUoF8M2pGp8zATliJ4u1yM0fa)

`$(cat /sys/kernel/mm/ksm/pages_sharing)` reported a peak value of 102399.

# Task 04 - Intel PIN

## Task A - Setup

```bash
$ cd ../minspect/
minspect$ ./setup.sh
~/Programs/performance-evaluation/lab-02/minspect/third_party ~/Programs/performance-evaluation/lab-02/minspect
--2022-10-21 23:34:53--  https://software.intel.com/sites/landingpage/pintool/downloads/pin-3.24-98612-g6bd5931f2-gcc-linux.tar.gz
Resolving software.intel.com (software.intel.com)... 2a02:26f0:9c00:19a::b, 2a02:26f0:9c00:1a0::b, 2a02:26f0:9c00:180::b, ...
Connecting to software.intel.com (software.intel.com)|2a02:26f0:9c00:19a::b|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27197980 (26M) [application/octet-stream]
Saving to: ‘pin-3.24-98612-g6bd5931f2-gcc-linux.tar.gz’

pin-3.24-98612-g6bd5931f2-g 100%[==========================================>]  25,94M  3,95MB/s    in 6,6s    

2022-10-21 23:34:59 (3,92 MB/s) - ‘pin-3.24-98612-g6bd5931f2-gcc-linux.tar.gz’ saved [27197980/27197980]

~/Programs/performance-evaluation/lab-02/minspect
minispect$ patch src/minspect.cpp patches/Task-A.patch
patching file src/minspect.cpp
```

## Task B - Instrumentation Callbacks

```bash
$ make
...
$ ./third_party/pin-3.24/pin -t obj-intel64/minspect.so -- ls -l 1>/dev/null 
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3090 -- mov rdi, rsp
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3093 -- call 0x7fee638d3de0
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3de0 -- push rbp
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3de1 -- mov rbp, rsp
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3de4 -- push r15
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3de6 -- mov r15, rdi
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3de9 -- push r14
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3deb -- push r13
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3ded -- push r12
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3def -- push rbx
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3df0 -- sub rsp, 0x38
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3df4 -- rdtsc 
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3df6 -- shl rdx, 0x20
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3dfa -- or rax, rdx
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3dfd -- lea rdx, ptr [rip+0x29074]
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3e04 -- mov qword ptr [rip+0x28775], rax
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3e0b -- mov rax, qword ptr [rip+0x29066]
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3e12 -- mov r12, rdx
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3e15 -- sub r12, qword ptr [rip+0x291e4]
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3e1c -- mov qword ptr [rip+0x29bd5], rdx
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3e23 -- mov qword ptr [rip+0x29bbe], r12
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3e2a -- test rax, rax
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3e2d -- jz 0x7fee638d3e9e
[minspect] /lib64/ld-linux-x86-64.so.2:.text:.text:7fee638d3e2f -- mov edi, 0x6fffffff
...
minspect$
minspect$
minspect$ patch src/minspect.cpp patches/Task-B.patch
```

## Task C - Analysis Callbacks (Read)

```bash
minspect$ make
...
minspect$ ./third_party/pin-3.24/pin -t obj-intel64/minspect.so -- ls -l 1>/dev/null 
[minspect] READ  | 0x00007f29c508ae0b: mov rax, qword ptr [rip+0x29066]         -- [ 0e 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae15: sub r12, qword ptr [rip+0x291e4]         -- [ 78 ae 02 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ 04 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ f5 fe ff 6f 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae7a: mov rax, qword ptr [rdx+0x10]            -- [ 05 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ 06 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ 0a 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ 0b 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ 03 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ 02 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ 14 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ 17 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ 07 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ 08 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ 09 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae91: mov rax, qword ptr [rdx+0x10]            -- [ fc ff ff 6f 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae7a: mov rax, qword ptr [rdx+0x10]            -- [ fd ff ff 6f 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae7a: mov rax, qword ptr [rdx+0x10]            -- [ f0 ff ff 6f 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae7a: mov rax, qword ptr [rdx+0x10]            -- [ f9 ff ff 6f 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508ae7a: mov rax, qword ptr [rdx+0x10]            -- [ 00 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508aea7: mov rax, qword ptr [rip+0x29b9a]         -- [ 88 3e 0b c5 29 7f 00 00 ]
[minspect] READ  | 0x00007f29c508aeb3: add qword ptr [rax+0x8], r12             -- [ 60 02 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508aeb7: mov rax, qword ptr [rip+0x29b82]         -- [ e8 3e 0b c5 29 7f 00 00 ]
[minspect] READ  | 0x00007f29c508aec3: add qword ptr [rax+0x8], r12             -- [ 00 b0 02 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508aec7: mov rax, qword ptr [rip+0x29b82]         -- [ a8 3e 0b c5 29 7f 00 00 ]
[minspect] READ  | 0x00007f29c508aed3: add qword ptr [rax+0x8], r12             -- [ 60 07 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f29c508aed7: mov rax, qword ptr [rip+0x29b7a]         -- [ b8 3e 0b c5 29 7f 00 00 ]
[minspect] READ  | 0x00007f29c508aee3: add qword ptr [rax+0x8], r12             -- [ 30 04 00 00 00 00 00 00 ]
...
minspect$
minspect$
minspect$ patch src/minspect.cpp patches/Task-D.patch
patching file src/minspect.cpp
```

## Task D - Analysis Callbacks (Write)

```bash
minspect$ make
...
minspect$ ./third_party/pin-3.24/pin -t obj-intel64/minspect.so -- ls -l 1>/dev/null
minspect$ ./third_party/pin-3.24/pin -t obj-intel64/minspect.so -- ls -l 1>/dev/null 
[minspect] WRITE | 0x00007faf3a3f9de0: push rbp                                 -- [ 00 00 00 00 00 00 00 00 ] ==> [ 00 00 00 00 00 00 00 00 ]
[minspect] WRITE | 0x00007faf3a3f9de4: push r15                                 -- [ 00 00 00 00 00 00 00 00 ] ==> [ 00 00 00 00 00 00 00 00 ]
[minspect] WRITE | 0x00007faf3a3f9de9: push r14                                 -- [ 00 00 00 00 00 00 00 00 ] ==> [ 00 00 00 00 00 00 00 00 ]
[minspect] WRITE | 0x00007faf3a3f9deb: push r13                                 -- [ 00 00 00 00 00 00 00 00 ] ==> [ 00 00 00 00 00 00 00 00 ]
[minspect] WRITE | 0x00007faf3a3f9ded: push r12                                 -- [ 00 00 00 00 00 00 00 00 ] ==> [ 00 00 00 00 00 00 00 00 ]
[minspect] WRITE | 0x00007faf3a3f9def: push rbx                                 -- [ 00 00 00 00 00 00 00 00 ] ==> [ 00 00 00 00 00 00 00 00 ]
[minspect] WRITE | 0x00007faf3a3f9e04: mov qword ptr [rip+0x28775], rax         -- [ 00 00 00 00 00 00 00 00 ] ==> [ 25 83 9f b5 d8 07 00 00 ]
[minspect] READ  | 0x00007faf3a3f9e0b: mov rax, qword ptr [rip+0x29066]         -- [ 0e 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007faf3a3f9e15: sub r12, qword ptr [rip+0x291e4]         -- [ 78 ae 02 00 00 00 00 00 ]
[minspect] WRITE | 0x00007faf3a3f9e1c: mov qword ptr [rip+0x29bd5], rdx         -- [ 00 00 00 00 00 00 00 00 ] ==> [ 78 2e 42 3a af 7f 00 00 ]
...
minspect$
minspect$
minspect$ patch src/minspect.cpp patches/Task-D.patch
patching file src/minspect.cpp
```

## Task E - Finishing Touches

```bash
minispect$ ldd /bin/ls
        linux-vdso.so.1 (0x00007ffc60dbd000)
        libselinux.so.1 => /lib/x86_64-linux-gnu/libselinux.so.1 (0x00007fa1e82b2000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fa1e80dd000)
        libpcre2-8.so.0 => /lib/x86_64-linux-gnu/libpcre2-8.so.0 (0x00007fa1e8045000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fa1e803f000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fa1e8338000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fa1e801d000)
minispect$ ./third_party/pin-3.24/pin -t obj-intel64/minspect.so -i /lib/x86_64-linux-gnu/libc.so.6 -- ls -l 1>/dev/null 
[minspect] READ  | 0x00007f96fcd0b118: ret                                      -- [ 21 2a b0 fc 96 7f 00 00 ]
[minspect] WRITE | 0x00007f96fcc9ae60: push rbx                                 -- [ 3b 00 00 00 00 00 00 00 ] ==> [ b0 74 f5 fc 96 7f 00 00 ]
[minspect] WRITE | 0x00007f96fcc9ae69: mov qword ptr [rip+0x14fcc0], rdi        -- [ 00 00 00 00 00 00 00 00 ] ==> [ 08 d4 b1 fc 96 7f 00 00 ]
[minspect] WRITE | 0x00007f96fcc9aec0: push r12                                 -- [ ff ff ff ff 00 00 00 00 ] ==> [ 00 01 00 00 40 00 00 00 ]
[minspect] WRITE | 0x00007f96fcc9aec5: push rbp                                 -- [ 00 01 00 00 40 00 00 00 ] ==> [ 00 00 00 00 00 00 00 00 ]
[minspect] WRITE | 0x00007f96fcc9aec9: push rbx                                 -- [ 00 00 00 00 00 00 00 00 ] ==> [ 80 03 00 00 80 03 00 00 ]
[minspect] READ  | 0x00007f96fcc9aed1: mov eax, dword ptr fs:[0x18]             -- [ 00 00 00 00 ]
[minspect] READ  | 0x00007f96fcc9aee6: cmpxchg dword ptr [rip+0x14fc53], edx    -- [ 00 00 00 00 ]
[minspect] WRITE | 0x00007f96fcc9aee6: cmpxchg dword ptr [rip+0x14fc53], edx    -- [ 00 00 00 00 ] ==> [ 01 00 00 00 ]
[minspect] READ  | 0x00007f96fcc9aeed: cmp byte ptr [rip+0x14fc50], 0x0         -- [ 00 ]
[minspect] WRITE | 0x00007f96fcc9aef6: mov byte ptr [rip+0x14fc47], 0x1         -- [ 00 ] ==> [ 01 ]
[minspect] WRITE | 0x00007f96fcc9af04: mov qword ptr [rip+0x14fc59], 0x30       -- [ 00 00 00 00 00 00 00 00 ] ==> [ 30 00 00 00 00 00 00 00 ]
[minspect] WRITE | 0x00007f96fcc9af0f: mov qword ptr [rip+0x14fc5a], rax        -- [ 00 00 00 00 00 00 00 00 ] ==> [ 78 ab de fc 96 7f 00 00 ]
[minspect] READ  | 0x00007f96fcc9af23: add r8, qword ptr [rip+0x14fc46]         -- [ 78 ab de fc 96 7f 00 00 ]
[minspect] WRITE | 0x00007f96fcc9af2a: mov qword ptr [rip+0x14fc2f], rax        -- [ 00 00 00 00 00 00 00 00 ] ==> [ 01 00 00 00 00 00 00 00 ]
[minspect] WRITE | 0x00007f96fcc9af36: mov qword ptr [r8], rbp                  -- [ 00 00 00 00 00 00 00 00 ] ==> [ 00 00 00 00 00 00 00 00 ]
[minspect] WRITE | 0x00007f96fcc9af39: mov qword ptr [r8+0x8], rbx              -- [ 00 00 00 00 00 00 00 00 ] ==> [ 00 00 00 00 00 00 00 00 ]
[minspect] WRITE | 0x00007f96fcc9af3d: mov qword ptr [r8+0x10], r12             -- [ 00 00 00 00 00 00 00 00 ] ==> [ 80 32 b0 fc 96 7f 00 00 ]
[minspect] WRITE | 0x00007f96fcc9af41: mov qword ptr [r8+0x18], rcx             -- [ 00 00 00 00 00 00 00 00 ] ==> [ 00 00 00 00 00 00 00 00 ]
[minspect] READ  | 0x00007f96fcc9af45: mov eax, dword ptr fs:[0x18]             -- [ 00 00 00 00 ]
[minspect] READ  | 0x00007f96fcc9af55: sub dword ptr [rip+0x14fbe4], 0x1        -- [ 01 00 00 00 ]
```

# Task 05 - Feedback

```bash
$ firefox https://forms.gle/LWBWYsMiJq8FsYdN9
$ date | md5sum
256f0bc1f3742ab73553fc06d0c5bf3e  -
```

Note I am using Bucharest local configuration.
