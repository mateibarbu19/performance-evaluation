import numpy as np
import matplotlib.pyplot as plt

data = [
    [0.266873, 0.329129, 0.330225, 0.456149, 2.267001, 2.263103],
    [0.267344, 0.397377, 0.270254, 0.281078, 1.470244, 2.219766],
    [0.994039, 0.515916, 0.409758, 0.484845, 0.415805, 0.205531]
]

X = np.arange(6)
ax = plt.subplot()

ax.bar(X + 0.00, data[0], color='b', width=0.25,
       label='Equal distribution of requests')
ax.bar(X + 0.25, data[1], color='g', width=0.25,
       label='Random distribution of requests')
ax.bar(X + 0.50, data[2], color='r', width=0.25,
       label='Throughput weighted distribution of requests')

ax.set_xticks(X + 0.25)
ax.set_xticklabels(X + 1)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.xlabel("Host number for each server", fontsize=16)
plt.ylabel("Average respone time (seconds)", fontsize=16)
plt.title(
    "Comparison of average response time of each server depending on scheduling",
    fontweight='bold', fontsize=20)
ax.legend(loc='best', fancybox=True)
plt.gcf().set_size_inches(14.6, 7)
plt.savefig('chart.png')
