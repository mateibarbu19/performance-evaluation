# Primer / Reminder

## `tcpdump`

```bash
$ sudo tcpdump -i wlp2s0 --number --nano --packet-buffered -X
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on wlp2s0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
    1  16:52:50.188789878 IP matei-debian.46175 > 66.22.244.6.50015: UDP, length 43
        0x0000:  4500 0047 da78 4000 4011 6800 c0a8 0168  E..G.x@.@.h....h
        0x0010:  4216 f406 b45f c35f 0033 f871 9078 d175  B...._._.3.q.x.u
        0x0020:  20e3 7d9e 0019 10e2 bede 0001 ad3a df4a  ..}..........:.J
        0x0030:  c80b 97b7 8a1a fc0c 0d91 ad0c d5c4 f3ea  ................
        0x0040:  1391 07c1 3a00 80                        ....:..
    2  16:52:50.190906511 IP 66.22.244.6.50015 > matei-debian.46175: UDP, length 201
        0x0000:  45a0 00e5 b1b5 4000 3711 9885 4216 f406  E.....@.7...B...
        0x0010:  c0a8 0168 c35f b45f 00d1 09c5 9078 b3d6  ...h._._.....x..
        0x0020:  c4b5 9ff5 0019 1125 bede 0001 6e9c 4da3  .......%....n.M.
        0x0030:  9dd3 12ed b189 4e0c bf25 f729 fe64 2979  ......N..%.).d)y
        0x0040:  fdeb b32f 661c 2c18 a377 5bce b68c ed4c  .../f.,..w[....L
        0x0050:  0031 a797 5439 7ac1 01f4 01e5 648a b7cc  .1..T9z.....d...
        0x0060:  c8a5 cca9 82e0 db02 3a35 4963 3d76 e0c1  ........:5Ic=v..
        0x0070:  5b40 1c4f 29ab dd6d 8e24 a00c 2765 0631  [@.O)..m.$..'e.1
        0x0080:  c4b6 eb4c 4166 1e44 9945 be9e 849d 61ec  ...LAf.D.E....a.
        0x0090:  e09b 0ea9 f77b 7906 79d9 2b62 f1f0 0f2d  .....{y.y.+b...-
        0x00a0:  7e71 81df c062 dda5 adb7 735c 94b6 3490  ~q...b....s\..4.
        0x00b0:  2eb0 dabf 5507 701f 3bdc e044 7e6d 83ab  ....U.p.;..D~m..
        0x00c0:  7895 25c9 6fc5 ff52 bf7f 6433 0cfa 9f73  x.%.o..R..d3...s
        0x00d0:  d64b 10d4 5cef c7af bb0d cac2 089b 3052  .K..\.........0R
        0x00e0:  4e0f 1400 00                             N....
```

## `tcpdump`

```bash
$ sudo iptables -A OUTPUT -p tcp -j LOG --log-prefix "EP" --sport 32768:60999 -m owner --uid-owner 0
$ sudo iptables -L OUTPUT --line-numbers
Chain OUTPUT (policy ACCEPT)
num  target     prot opt source               destination         
1    LOG        tcp  --  anywhere             anywhere             tcp spts:32768:60999 owner UID match root LOG level warning prefix "EP"
$ sudo curl www.google.com   
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ro"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="jEAwLjSc16FVpMA3MqMkPA">(function(){window.google={kEI:'QTFlY4yMLO2Axc8Pi6GK6AY',kEXPI:'0,1302536,56873,6058,207,4804,2316,383,246,5,5367,1123753,1578490,16115,28684,22430,1362,12319,17580,4998,13228,3847,10622,22741,5081,1593,1279,2742,149,1103,840,1983,213,4101,109,3405,606,2023,1733,43,521,14670,3227,2845,7,29075,4695,1851,6398,9358,3,576,6460,148,13975,4,1528,2304,7039,27731,7357,13658,4437,16786,5830,2527,4097,14,4035,3,3541,1,11943,2318,27893,2,28138,11623,5679,1020,2378,12488,16256,4569,6255,23421,1252,5835,14968,4332,5017,2467,17756,9326,8155,7381,15969,874,7829,11803,8,1922,5784,3995,6542,15237,2,9541,4832,2523,14615,700,4,2,2,2,2,2,1,1,5335,85,3230,90,5173,3530,6812,3246,1381,1757,951,1182,751,201,1867,7796,1944,627,1461,869,459,341,1622,2448,1158,2024,1125,792,746,3209,90,210,3084,778,81,22,224,33,3211,2411,1064,677,814,2894,382,584,1120,381,565,404,587,544,425,1356,124,86,921,444,7,487,95,327,7,389,183,610,748,24,373,109,956,144,9,3,367,268,1,134,387,115,480,312,399,4,19,252,19,229,2,2,1455,235,920,20,1338,347,238,25,8,306,373,1,781,3,59,1080,199,97,943,860,335,38,2,182,328,145,200,93,100,31,323,591,531,694,634,1280,5302768,5978,5994070,1695,2803384,3306,141,795,19735,1,1,346,2277,134,20,38,19,23947997,486,26,26,4041604,5058,13579,3405,10285,1034,2494',kBL:'9vel'};google.sn='webhp';google.kHL='ro';})();(function(){
var f=this||self;var h,k=[];function l(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||h}function m(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b}
$ sudo dmesg | tail 
[ 3067.913957] EPIN= OUT=wlp2s0 SRC=192.168.1.104 DST=162.159.138.234 LEN=127 TOS=0x00 PREC=0x00 TTL=64 ID=11303 DF PROTO=TCP SPT=58152 DPT=443 WINDOW=501 RES=0x00 ACK PSH URGP=0 
[ 3127.914129] EPIN= OUT=wlp2s0 SRC=192.168.1.104 DST=142.250.186.68 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=57845 DF PROTO=TCP SPT=48020 DPT=80 WINDOW=64240 RES=0x00 SYN URGP=0 
[ 3127.951369] EPIN= OUT=wlp2s0 SRC=192.168.1.104 DST=142.250.186.68 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=57846 DF PROTO=TCP SPT=48020 DPT=80 WINDOW=502 RES=0x00 ACK URGP=0 
[ 3127.951584] EPIN= OUT=wlp2s0 SRC=192.168.1.104 DST=142.250.186.68 LEN=130 TOS=0x00 PREC=0x00 TTL=64 ID=57847 DF PROTO=TCP SPT=48020 DPT=80 WINDOW=502 RES=0x00 ACK PSH URGP=0 
[ 3128.056566] EPIN= OUT=wlp2s0 SRC=192.168.1.104 DST=142.250.186.68 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=57848 DF PROTO=TCP SPT=48020 DPT=80 WINDOW=493 RES=0x00 ACK URGP=0 
[ 3128.056678] EPIN= OUT=wlp2s0 SRC=192.168.1.104 DST=142.250.186.68 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=57849 DF PROTO=TCP SPT=48020 DPT=80 WINDOW=439 RES=0x00 ACK URGP=0 
[ 3128.070971] EPIN= OUT=wlp2s0 SRC=192.168.1.104 DST=142.250.186.68 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=57850 DF PROTO=TCP SPT=48020 DPT=80 WINDOW=493 RES=0x00 ACK URGP=0 
[ 3128.071033] EPIN= OUT=wlp2s0 SRC=192.168.1.104 DST=142.250.186.68 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=57851 DF PROTO=TCP SPT=48020 DPT=80 WINDOW=461 RES=0x00 ACK URGP=0 
[ 3128.089240] EPIN= OUT=wlp2s0 SRC=192.168.1.104 DST=142.250.186.68 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=57852 DF PROTO=TCP SPT=48020 DPT=80 WINDOW=477 RES=0x00 ACK URGP=0 
[ 3128.089832] EPIN= OUT=wlp2s0 SRC=192.168.1.104 DST=142.250.186.68 LEN=52 TOS=0x00 PREC=0x00 TTL=64 ID=57853 DF PROTO=TCP SPT=48020 DPT=80 WINDOW=501 RES=0x00 ACK FIN URGP=0 
```

[![Minimum TTL to make DNS work](https://asciinema.org/a/R9UK491CgZVpRbSfMLey1DGc2.svg)](https://asciinema.org/a/R9UK491CgZVpRbSfMLey1DGc2)

[Bypassing `iptables`](https://github.com/rtsisyk/linux-iptables-contrack-exploit).

# Network Exploration

```bash
$ ip -c neigh show
192.168.100.26 dev wlp2s0 lladdr 9e:09:69:54:51:21 REACHABLE
192.168.100.1 dev wlp2s0 lladdr 30:d1:7e:e0:29:4c REACHABLE
fe80::1 dev wlp2s0 lladdr 30:d1:7e:e0:29:4c router REACHABLE
```

Wireshark capture using `arp-scan`:

```python
No.     Time           Source                Destination           Protocol Length Info
      1 0.000000000    9e:09:69:54:51:21     IntelCor_f8:9f:49     ARP      42     Who has 192.168.100.20? Tell 192.168.100.26

Frame 1: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: 9e:09:69:54:51:21 (9e:09:69:54:51:21), Dst: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      2 0.000023106    IntelCor_f8:9f:49     9e:09:69:54:51:21     ARP      42     192.168.100.20 is at f8:ac:65:f8:9f:49

Frame 2: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: 9e:09:69:54:51:21 (9e:09:69:54:51:21)
Address Resolution Protocol (reply)

No.     Time           Source                Destination           Protocol Length Info
      3 1.864625268    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.0? Tell 192.168.100.20

Frame 3: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      4 1.866966965    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.1? Tell 192.168.100.20

Frame 4: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      5 1.868774740    HuaweiTe_e0:29:4c     IntelCor_f8:9f:49     ARP      42     192.168.100.1 is at 30:d1:7e:e0:29:4c

Frame 5: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: HuaweiTe_e0:29:4c (30:d1:7e:e0:29:4c), Dst: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49)
Address Resolution Protocol (reply)

No.     Time           Source                Destination           Protocol Length Info
      6 1.868996721    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.2? Tell 192.168.100.20

Frame 6: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      7 1.870562940    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.3? Tell 192.168.100.20

Frame 7: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      8 1.872133911    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.4? Tell 192.168.100.20

Frame 8: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      9 1.874134438    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.5? Tell 192.168.100.20

Frame 9: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     10 1.876670965    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.6? Tell 192.168.100.20

Frame 10: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     11 1.879145655    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.7? Tell 192.168.100.20

Frame 11: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     12 1.881188528    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.8? Tell 192.168.100.20

Frame 12: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     13 1.882679852    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.9? Tell 192.168.100.20

Frame 13: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     14 1.884065802    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.10? Tell 192.168.100.20

Frame 14: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     15 1.886190438    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.11? Tell 192.168.100.20

Frame 15: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     16 1.888777380    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.12? Tell 192.168.100.20

Frame 16: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     17 1.891115100    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.13? Tell 192.168.100.20

Frame 17: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     18 1.892970332    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.14? Tell 192.168.100.20

Frame 18: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     19 1.894492053    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.15? Tell 192.168.100.20

Frame 19: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     20 1.896180788    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.16? Tell 192.168.100.20

Frame 20: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     21 1.898385489    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.17? Tell 192.168.100.20

Frame 21: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     22 1.900837492    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.18? Tell 192.168.100.20

Frame 22: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     23 1.903130580    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.19? Tell 192.168.100.20

Frame 23: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     24 1.905118159    IntelCor_f8:9f:49     Broadcast             ARP      42     ARP Announcement for 192.168.100.20

Frame 24: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (ARP Announcement)

No.     Time           Source                Destination           Protocol Length Info
     25 1.906696324    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.21? Tell 192.168.100.20

Frame 25: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)
```

Wireshark capture using a custom script:

```bash
$ ./localnet-ping.sh wlp2s0
  192.168.100.1    HUAWEI TECHNOLOGIES CO.,LTD        ==>  ok
```

```python
No.     Time           Source                Destination           Protocol Length Info
      1 0.000000000    IntelCor_f8:9f:49     9e:09:69:54:51:21     ARP      42     Who has 192.168.100.26? Tell 192.168.100.20

Frame 1: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: 9e:09:69:54:51:21 (9e:09:69:54:51:21)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      2 0.005395540    9e:09:69:54:51:21     IntelCor_f8:9f:49     ARP      42     192.168.100.26 is at 9e:09:69:54:51:21

Frame 2: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: 9e:09:69:54:51:21 (9e:09:69:54:51:21), Dst: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49)
Address Resolution Protocol (reply)

No.     Time           Source                Destination           Protocol Length Info
      3 0.086490854    9e:09:69:54:51:21     IntelCor_f8:9f:49     ARP      42     Who has 192.168.100.20? Tell 192.168.100.26

Frame 3: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: 9e:09:69:54:51:21 (9e:09:69:54:51:21), Dst: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      4 0.086507800    IntelCor_f8:9f:49     9e:09:69:54:51:21     ARP      42     192.168.100.20 is at f8:ac:65:f8:9f:49

Frame 4: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: 9e:09:69:54:51:21 (9e:09:69:54:51:21)
Address Resolution Protocol (reply)

No.     Time           Source                Destination           Protocol Length Info
      5 0.681128113    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.0? Tell 192.168.100.20

Frame 5: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      6 0.683293727    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.1? Tell 192.168.100.20

Frame 6: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      7 0.685282758    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.2? Tell 192.168.100.20

Frame 7: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      8 0.687230770    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.3? Tell 192.168.100.20

Frame 8: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
      9 0.689074778    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.4? Tell 192.168.100.20

Frame 9: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     10 0.691144451    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.5? Tell 192.168.100.20

Frame 10: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     11 0.693140257    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.6? Tell 192.168.100.20

Frame 11: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     12 0.695145362    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.7? Tell 192.168.100.20

Frame 12: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     13 0.697058266    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.8? Tell 192.168.100.20

Frame 13: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     14 0.699110193    HuaweiTe_e0:29:4c     IntelCor_f8:9f:49     ARP      42     192.168.100.1 is at 30:d1:7e:e0:29:4c

Frame 14: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: HuaweiTe_e0:29:4c (30:d1:7e:e0:29:4c), Dst: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49)
Address Resolution Protocol (reply)

No.     Time           Source                Destination           Protocol Length Info
     15 0.699293396    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.9? Tell 192.168.100.20

Frame 15: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     16 0.701312834    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.10? Tell 192.168.100.20

Frame 16: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     17 0.703081849    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.11? Tell 192.168.100.20

Frame 17: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     18 0.704873330    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.12? Tell 192.168.100.20

Frame 18: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     19 0.707016715    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.13? Tell 192.168.100.20

Frame 19: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     20 0.709212397    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.14? Tell 192.168.100.20

Frame 20: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     21 0.711515720    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.15? Tell 192.168.100.20

Frame 21: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     22 0.713410954    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.16? Tell 192.168.100.20

Frame 22: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     23 0.715030607    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.17? Tell 192.168.100.20

Frame 23: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     24 0.716824567    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.18? Tell 192.168.100.20

Frame 24: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     25 0.718913658    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.19? Tell 192.168.100.20

Frame 25: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time           Source                Destination           Protocol Length Info
     26 0.721300310    IntelCor_f8:9f:49     Broadcast             ARP      42     ARP Announcement for 192.168.100.20

Frame 26: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (ARP Announcement)

No.     Time           Source                Destination           Protocol Length Info
     27 0.723618671    IntelCor_f8:9f:49     Broadcast             ARP      42     Who has 192.168.100.21? Tell 192.168.100.20

Frame 27: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlp2s0, id 0
Ethernet II, Src: IntelCor_f8:9f:49 (f8:ac:65:f8:9f:49), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)
```

## `nmap` vs `traceroute`

```bash
$ sudo nmap                            \
    -sn     `# disable port scan`      \
    -Pn     `# disable host discovery` \
    -tr     `# perform traceroute`     \
    8.8.8.8
Starting Nmap 7.80 ( https://nmap.org ) at 2022-11-04 23:04 EET
Nmap scan report for dns.google (8.8.8.8)
Host is up (0.024s latency).

TRACEROUTE (using proto 1/icmp)
HOP RTT      ADDRESS
1   6.68 ms  192.168.100.1
2   10.89 ms StamAcasa.rdsnet.ro (10.0.0.1)
3   10.38 ms qr90.bucuresti.rdsnet.ro (172.19.210.193)
4   11.49 ms 10.220.199.26
5   26.01 ms 10.220.178.148
6   25.32 ms 209.85.168.182
7   27.01 ms 74.125.242.225
8   24.69 ms 142.251.228.23
9   24.17 ms dns.google (8.8.8.8)

Nmap done: 1 IP address (1 host up) scanned in 0.17 seconds
```

```bash
$ traceroute 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  _gateway (192.168.100.1)  3.426 ms  10.661 ms  10.541 ms
 2  StamAcasa.rdsnet.ro (10.0.0.1)  10.463 ms  10.384 ms  10.308 ms
 3  qr90.bucuresti.rdsnet.ro (172.19.210.193)  10.211 ms  10.643 ms  11.156 ms
 4  10.220.158.66 (10.220.158.66)  15.531 ms 10.220.199.12 (10.220.199.12)  11.709 ms 10.220.199.24 (10.220.199.24)  12.261 ms
 5  10.220.156.5 (10.220.156.5)  20.942 ms 10.220.153.18 (10.220.153.18)  22.598 ms 10.220.156.5 (10.220.156.5)  19.157 ms
 6  72.14.216.212 (72.14.216.212)  20.717 ms 209.85.168.182 (209.85.168.182)  18.279 ms 72.14.216.212 (72.14.216.212)  16.139 ms
 7  * 74.125.242.225 (74.125.242.225)  21.409 ms *
 8  216.239.35.185 (216.239.35.185)  23.266 ms dns.google (8.8.8.8)  17.523 ms  23.116 ms
```

The differences I noticed are that `nmap` pings the destination and takes into
account a Time-to-live exceeded message, but `traceroute` tries to send
UDP messages and standard DNS queries, and when receiving a Time-to-live
exceeded message dynamically changes it's strategy.

# Protocol Options

## Injecting IP Options

```bash
$ git clone https://github.com/RaduMantu/ops-inject.git
Cloning into 'ops-inject'...
remote: Enumerating objects: 224, done.
remote: Counting objects: 100% (224/224), done.
remote: Compressing objects: 100% (140/140), done.
remote: Total 224 (delta 101), reused 201 (delta 78), pack-reused 0
Receiving objects: 100% (224/224), 366.00 KiB | 2.15 MiB/s, done.
Resolving deltas: 100% (101/101), done.
$ cd !$:t:r
cd ops-inject
ops-inject$ make -j $(nproc)
gcc -c -I include  -o obj/str_proto.o src/str_proto.c
g++  -o bin/ops-inject obj/cli_args.o obj/decoders.o obj/main.o obj/reassemblers.o obj/csum.o obj/ops_ip.o obj/ops_tcp.o obj/ops_udp.o obj/str_proto.o -lnetfilter_queue -lnfnetlink
ops-inject$ sudo iptables -I OUTPUT -p icmp -j NFQUEUE --queue-num 0 --queue-bypass
ops-inject$ sudo iptables -L OUTPUT --line-numbers
Chain OUTPUT (policy ACCEPT)
num  target     prot opt source               destination         
1    NFQUEUE    icmp --  anywhere             anywhere             NFQUEUE num 0 bypass
ops-inject$ sudo su
ops-inject$ ./bin/ops-inject -p ip -q 0 -w <(printf '\x07')
[*] src/main.cpp:159 Parsed cli arguments
[*] src/main.cpp:164 Opened nfq handle
[*] src/main.cpp:170 Bound nfq handle to queue
[*] src/main.cpp:175 Set copy packet mode
[*] src/main.cpp:189 Starting main loop
```

Unfortunately, this isn't working even inside a RoEduNet network, as shown in my
`traceroute` log. 

```bash
$ traceroute 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  _gateway (192.168.1.1)  1.935 ms  1.849 ms  1.825 ms
 2  172.16.7.254 (172.16.7.254)  4.086 ms  4.064 ms  4.037 ms
 3  141.85.225.2 (141.85.225.2)  2.794 ms  2.762 ms  2.740 ms
 4  172.31.255.33 (172.31.255.33)  4.184 ms  4.141 ms  4.087 ms
 5  37.128.225.233 (37.128.225.233)  4.646 ms  4.584 ms  5.718 ms
 6  37.128.232.181 (37.128.232.181)  4.489 ms  3.014 ms  2.928 ms
 7  hu-0-0-0-0.core3.nat.roedu.net (37.128.239.101)  3.890 ms  3.651 ms  6.814 ms
 8  te-0-6-0-1.peers1.nat.roedu.net (37.128.239.42)  4.581 ms  4.551 ms  4.525 ms
 9  google.interlan.ro (86.104.125.129)  31.796 ms  32.855 ms  31.738 ms
10  108.170.252.65 (108.170.252.65)  31.716 ms  33.868 ms 108.170.251.193 (108.170.251.193)  30.627 ms
11  142.250.214.203 (142.250.214.203)  30.576 ms 142.250.214.201 (142.250.214.201)  30.554 ms 142.250.236.57 (142.250.236.57)  30.665 ms
12  dns.google (8.8.8.8)  32.379 ms  32.342 ms  33.330 ms
$ ping -c 3 $(dig +short digitalocean.com | head -n 1)
    PING 104.16.182.15 (104.16.182.15) 56(84) bytes of data.
    64 bytes from 104.16.182.15: icmp_seq=1 ttl=57 time=46.7 ms
    RR:     141.85.13.15
            37.128.225.226
            37.128.232.178
            37.128.232.177
            80.97.248.33
            162.158.16.1
            104.16.182.15
            104.16.182.15
            162.158.16.1
PING 104.16.181.15 (104.16.181.15) 56(84) bytes of data.

--- 104.16.181.15 ping statistics ---
3 packets transmitted, 0 received, 100% packet loss, time 2045ms
```

# Feedback

```bash
$ firefox https://forms.gle/LWBWYsMiJq8FsYdN9
$ date | md5sum
9634c4060a0bc9ad97afb9679e596a38  -
```