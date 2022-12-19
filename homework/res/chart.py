import numpy as np
import matplotlib.pyplot as plt

data = [
    [266873, 329129, 330225, 456149, 2267001, 2263103],
    [267344, 397377, 270254, 281078, 1470244, 2219766],
    [994039, 515916, 409758, 484845, 415805, 205531]
]

X = np.arange(6)
print(X)
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
plt.ylabel("Average respone time (microseconds)", fontsize=16)
plt.title(
    "Comparison of average response time of each server depending on scheduling",
    fontweight='bold', fontsize=20)
ax.legend(loc='best', fancybox=True)
plt.gcf().set_size_inches(14.6, 7)
plt.savefig('chart.png')
