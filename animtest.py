from libs import *


i = Intersection()

i.spawncars(n = 3)

algo = NetworkAlgorithm(i)

algo.runsimulation(endtime=50)

timeline = algo.getrecord(listform = True)

for i in range(20, 21):
    print()
    firstframe = timeline[i]

    # print(firstframe)

    for k in firstframe.keys():
        print(k)
        for car in firstframe[k]:
            print(car)