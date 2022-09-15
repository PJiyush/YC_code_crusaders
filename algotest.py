from libs import *
import matplotlib.pyplot as plt
from copy import deepcopy

# i.green('right')

# print(i)

# y1s, y2s = [], []
# xs = []

k = 3
n=10

# for each in range(1, 10):
#     xs.append(each)
#     y1, y2 = 0, 0

#     for x in range(k):

#         i, j = Intersection(), Intersection()

#         i.spawncars(n=n)
#         j.spawncars(n=n)

#         simplealgo = SimpleCycle(i, period=each)
#         complexalgo = NetworkAlgorithm(j, thresh=each, onlyatintersection= True)

#         y1 += (simplealgo.runsimulation(150, verbose = False))
#         y2 += (complexalgo.runsimulation(150))


#     y1 /= k
#     y2 /= k

#     y1s.append(y1)
#     y2s.append(y2)

# print(f'stopped at {i.t}', len(i.getstoppedcars()))
# print(f'stopped at {j.t}', len(j.getstoppedcars()))

# print(i)
# i.printcars()

xs, ys = [], []

for each in range(1, 11):
    xs.append(each)

    i = Intersection()

    i.spawncars(n = 3)

    algo = NetworkAlgorithm(i, thresh=each)

    y = algo.runsimulation(endtime = 20, debug=True)

    ys.append(y)




plt.scatter(xs, ys, color='blue', alpha=0.4)
# plt.scatter(xs, y2s, color='green', alpha=0.4)
plt.ylabel("Average waiting time")
plt.xlabel("Period of light cycle")
plt.title(f"Algo Comparison, k = {k}, n = {n}")
# plt.legend(['Simple', 'Network'])
plt.show()