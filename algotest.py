from turtle import color
from libs import *
import matplotlib.pyplot as plt


# i.green('right')

# print(i)

ys = []
xs = []

for each in range(1, 50):
    xs.append(each)

    i = Intersection()

    i.spawncars(n=10)

    algo = SimpleCycle(i, period=each)

    ys.append(algo.runsimulation(600, verbose = False))

print(f'stopped at {i.t}', len(i.getstoppedcars()))

plt.scatter(xs, ys, color='blue', alpha=0.4)
plt.ylabel("Average waiting time")
plt.xlabel("Period of light cycle")
plt.title("Simple Cycle")
plt.show()