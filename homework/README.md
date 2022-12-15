# Prerequisites

## Mininet machine

```bash
$ sudo apt install mininet
$ sudo /usr/share/openvswitch/scripts/ovs-ctl start
```

## Run the topology

```bash
$ sudo python3 topology.py matei.barbu1905 -t
matei.barbu1905
...
Running base test with only one server
Done
*** Starting CLI:
stopping h1 
```

# Evaluation - System Limits Analysis

> How many requests can be handled by a single machine?

The ambiguity of this question, alongside with the technical particularities of
a network configuration make it impossible to answer or simulate. The biggest
problem arises from not knowing the network cards on each host. If it supports LSO @LWN_LSO then simple bandwidth information will not suffice. When using Mininet we face scheduling challenges, how threads are given CPU time, and which of these are chosen with respect to the hosts/clients interaction.

> What is the latency of each region?

- ASIA:
- EMEA:
- US:

> What is the server path with the smallest response time? But the slowest?

- Answer:

> What is the path that has the greatest loss percentage?

- Answer:

> What is the latency introduced by the first router in our path?

- Answer:

> Is there any bottleneck in the topology? How would you solve this issue?

- Answer:

> What is your estimation regarding the latency introduced?

- Answer:

> What downsides do you see in the current architecture design?

- Answer:

# Implementation

## Solution

## Efficient Policies Comparison

# Bibliography
