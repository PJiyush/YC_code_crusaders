from turtle import color
from libs import *
import matplotlib.pyplot as plt
import pickle

# minn, maxn = 50, 100
# period = 20

# endtime = 50

# xs1, ys1, zs1 = [], [], []

# k = 3

# for each in range(minn, maxn):

#     xs1.append(each)

#     y, z = 0, 0
#     for x in range(k):
#         i, j = Intersection(), Intersection()

#         i.spawncars(n = each)
#         j.spawncars(n = each)

#         na = NetworkAlgorithm(i, thresh = period)
#         oa = SimpleCycle(j, period = period)

#         y += na.runsimulation(endtime = endtime, record = False)
#         z += oa.runsimulation(endtime = endtime, record = False)

#     ys1.append(y/k)
#     zs1.append(z/k)

# with open('xs2.txt', 'rb') as file:
#     xs = pickle.load(file)
# with open('ys2.txt', 'rb') as file:
#     ys = pickle.load(file)
# with open('zs2.txt', 'rb') as file:
#     zs = pickle.load(file)

# k = 5
# n = 50

# ax = plt.axes()
# ax.set_facecolor((0.1, 0.1, 0.1))
# plt.plot(xs, ys, 'go-', alpha=1, color = (108/255, 245/255, 163/255))
# plt.plot(xs, zs, 'bo-', alpha=1, color = (108/255, 113/255, 245/255))
# plt.ylabel("Average waiting time")
# plt.xlabel("Period of light cycle")
# plt.title(f"Performance Comparison, k = {k}, n = {n}")
# plt.legend(['Network', 'Simple'])
# plt.show()