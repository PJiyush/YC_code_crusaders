from libs import *
import matplotlib.pyplot as plt


# i.green('right')

# print(i)

ys = []
xs = []

k = 3
n=10

for each in range(1, 50):
    xs.append(each)
    y = 0
    for x in range(k):

        i = Intersection()

        i.spawncars(n=n)

        algo = SimpleCycle(i, period=each)

        y += (algo.runsimulation(250, verbose = False))
    y /= k
    ys.append(y)

print(f'stopped at {i.t}', len(i.getstoppedcars()))


plt.scatter(xs, ys, color='blue', alpha=0.4)
plt.ylabel("Average waiting time")
plt.xlabel("Period of light cycle")
plt.title(f"Simple Cycle, k = {k}, n = {n}")
plt.show()