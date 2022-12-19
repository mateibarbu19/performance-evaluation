# Prerequisites

Contrary to official recommendation, I took the liberty of running this homework
on a native Linux machine (Debian $11$ with kernel `5.10.0-20-amd64`) with a
Intel i7-8550U processor and Python `3.9.2`.^[Because I don't know how much the
Mininet actually uses the network card, for all intents and purposes it is a
Intel Wireless-AC 9260 rev. 29.]

I have used a virtual machine only for bandwidth testing and for generating the
[`requirements.txt`](src/requirements.txt) file.

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

When answering any performance questions in this analysis, I measured the
latency of a route by dividing in half the average round trip time for a hundred
control packages (ICMP echo).  Note,  I chose not to filter any outliers,
because other (unknown to the user) control packages and internal host
parameters are expected to cause delays. Loss percentage was measured in the
same conditions. Keep in mind that latency is influenced by package loss (i.e.
latency is directly proportional to it).

Bandwidth, on the other hand, was provided by `iperf` (as a mininet built-in),
specifically it's first return value (i.e. the servers reported bandwidth). Bare
in mind that any tools which uses IP addresses cannot measure bandwidth between
a host and a switch. For reasons unknown to me, measurements could only be
performed on the virtual machine. For this reason I tested this part manually,
all of the rest being automated in [`test.py`](src/test.py)

> How many requests can be handled by a single machine?

The ambiguity of this question, alongside with the technical particularities of
a network configuration make it impossible to answer or simulate. The biggest
problem arises from not knowing the network cards on each host. If it supports
LSO @LWN_LSO then simple bandwidth information will not suffice. When using
Mininet we face scheduling challenges, how threads are given CPU time, and which
of these are chosen with respect to the hosts/clients interaction. In the end
this debate will be settled by the throughput of each servers connection to the
command unit. See table \ref{response-table} for values.

```{=latex}
\begin{table}
\center\begin{tabular}{c|c}
\hline

   
    Host     & Response procentage \\

\hline

\texttt{h1}  &        $99$         \\
\texttt{h2}  &        $23$         \\
\texttt{h3}  &        $31$         \\
\texttt{h4}  &        $66$         \\
\texttt{h5}  &        $2$          \\
\texttt{h6}  &        $2$          \\

\hline
\end{tabular}
\caption{\label{response-table}Ilustration of the procentage of responded
requests in a houndred sized batch (using the original \texttt{client.py}) with
a 2 second timeout.}
\end{table}
```

> What is the latency of each region?

I consider the latency for a region to be equal to the average latency any route
from the command unit to any host in that region (because there weren't any user
in the given topology). See table \ref{latency-table} for values, precision was
observed amongst runs.

```{=latex}
\begin{table}
\center\begin{tabular}{c|l}
\hline

  Region &  Latency (ms)  \\

\hline

  ASIA   &   $36.881$     \\
  EMEA   &   $43.34425$   \\
   US    &   $20.09025$   \\

\hline
\end{tabular}
\caption{\label{latency-table}Latency for each region.}
\end{table}
```

> What is the server path with the smallest response time? But the slowest?

USs top dollar acquired the most responsive servers, host $5$, as opposed to
EMEAs old-timer, host $4$.

> What is the path that has the greatest loss percentage?

The most (unique) packets lost are those intended for host $6$ along the path
starting from the command unit. While other hosts can rank the same as the
former, this result is the most consistent along multiple runs of the same test.
^[Decompiling the topology setup script, yields a different answer. However,
after thorough testing I have arrived at the conclusion that there is a
decoupling between the ping implementation (for example a moving window average)
and the analytical statistic approach, the result of which I was expecting.]

> What is the latency introduced by the first router in our path?

Without router $0$, I imagined that routers $1$, $2$ and $3$ would be connected
by a direct link to switch $0$. So the latency introduced by the first router
is equal to the average of all links from router $0$ to $1$, $2$ and $3$, which
I measured to be in the range of $8.8014$ to $11.911$, around $9$ most times.

> Is there any bottleneck in the topology? How would you solve this issue?

A bottleneck should be any low bandwidth connection. ^[Because a physical
bottleneck is any point in which flow is obstructed.] See table
\ref{bandwidth-table} for values. ^[Decompiling the topology setup script,
yields a higher value for all results. Given that all measurements had about the
same accuracy, the difference is tolerable.]

```{=latex}
\begin{table}
\center\begin{tabular}{c|c|c}
\hline

   Client   &     Server     & Bandwidth (Kbits/sec) \\

\hline

\texttt{c0}  &  \texttt{r0}  &       $19.6$           \\
\texttt{r1}  &  \texttt{h1}  &       $15.6$           \\
\texttt{r0}  &  \texttt{r2}  &       $12.7$           \\
\texttt{r0}  &  \texttt{r1}  &       $10.5$           \\

\hline\hline

\texttt{r0}  &  \texttt{r3}  &       $3.74$           \\
\texttt{r1}  &  \texttt{h2}  &       $1.72$           \\
\texttt{r2}  &  \texttt{h3}  &       $2.83$           \\
\texttt{r2}  &  \texttt{h4}  &       $2.85$           \\
\texttt{r3}  &  \texttt{h5}  &       $0.97$           \\
\texttt{r3}  &  \texttt{h6}  &       $1.83$           \\

\hline
\end{tabular}
\caption{\label{bandwidth-table}Bandwidth between two station, one acting like a
\texttt{iperf} client , and another like a server. Separated by a double
horizontal line, are on top the high bandwidth links and low ones below.}
\end{table}
```

A (kind of obvious) solution would be to change these links. Another,
(unreasonable and forced) idea is to add servers, as many as it takes, to
compensate for the limited requests/second throughput.

> What is your estimation regarding the latency introduced?

This one's trickier to answer. A naive approach was to calculate the latency
from switches $1$, $2$ and $3$ to their connected hosts, and subtract those
values from the latencies of the command unit accessing the same hosts. Such a
simple analysis will not suffice, because it doesn't take into account
scheduling latencies (inside the load balancer) and how many collision domains
are configured on the switch.

Given how I defined latency for each region to be, a rough approximation of "the
latency introduced" could be the average of tables \ref{latency-table} values,
$33.438$ ms.

> What downsides do you see in the current architecture design?

There is, without a doubt! The fact that every request passes through the
command unit. Let's say $1000$ "newly logged in" users in the US want to access
a server. And there are $2000$ users in ASIA in the same situation. So $3000$
requests will assault the control unit.

Another downside is the infrastructure cost. Given that the block `10.0.0.0/8`
is set aside for use in private networks @cotton2010special, this means the
servers in any region are inside the same private network.

A notable alternative is one based on anycasting (a bigger bang for your buck).
However there is no load balancing (or has inherit firewall problems).
@Anycast_TCP

# Implementation

Check out my implementation in `test.py`. Didn't have time to fill in this part.

## Solution

## Efficient Policies Comparison

# Bibliography
