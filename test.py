from libs import *

i = Intersection()
i.spawncars(3)
algo = NetworkAlgorithm(i)

algo.runsimulation(50)

print(len(algo.record))
r = algo.getrecord()

# for frame in r[:1]:
for lane in r[48].keys():
    print(lane)
    for car in r[48][lane]:
        print(car)
print()
print()
for lane in r[49].keys():
    print(lane)
    for car in r[49][lane]:
        print(car)