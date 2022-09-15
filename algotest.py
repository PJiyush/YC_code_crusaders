from libs import *
import matplotlib.pyplot as plt
from copy import deepcopy



k = 5
n = 50

xs, ys, zs = [], [], []

for each in range(1, 50):
    xs.append(each)
    y, z = 0, 0
    for x in range(k):
        print(f"Current threshold is : {each}")
        
        i, j = Intersection(), Intersection()

        i.spawncars(n = n)
        j.spawncars(n = n)

        nalgo = NetworkAlgorithm(i, thresh=each)
        oalgo = SimpleCycle(j, period=each)

        y += nalgo.runsimulation(endtime = 100, record = False)
        z += oalgo.runsimulation(endtime = 100, record = False)

    ys.append(y/k)
    zs.append(z/k)




plt.scatter(xs, ys, color='blue', alpha=0.4)
plt.scatter(xs, zs, color='green', alpha=0.4)
plt.ylabel("Average waiting time")
plt.xlabel("Period of light cycle")
plt.title(f"Performance Comparison, k = {k}, n = {n}")
plt.legend(['Network', 'Simple'])
plt.show()