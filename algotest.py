from libs import *
import matplotlib.pyplot as plt
from copy import deepcopy

# i.green('right')

# print(i)

y1s, y2s = [], []
xs = []

k = 5
n=10

for each in range(50, 150):
    xs.append(each)
    y1, y2 = 0, 0
    for x in range(k):

        i = Intersection()

        i.spawncars(n=n)

        i2 = deepcopy(i)

        simplealgo = SimpleCycle(i, period=each)
        complexalgo = NetworkAlgorithm(i2, thresh=each, onlywaiting=False)

        y1 += (simplealgo.runsimulation(250, verbose = False))
        y2 += (complexalgo.runsimulation(250))
    y1 /= k
    y2 /= k
    y1s.append(y1)
    y2s.append(y2)

print(f'stopped at {i.t}', len(i.getstoppedcars()))
print(f'stopped at {i2.t}', len(i2.getstoppedcars()))


plt.scatter(xs, y1s, color='blue', alpha=0.4)
plt.scatter(xs, y2s, color='green', alpha=0.4)
plt.ylabel("Average waiting time")
plt.xlabel("Period of light cycle")
plt.title(f"Simple Cycle, k = {k}, n = {n}")
plt.legend(['Simple Algorithm', 'Smart Algorithm'])
plt.show()