from libs import *

i = Intersection()
i.spawncars(3)
algo = NetworkAlgorithm(i)

algo.runsimulation(10)

record = algo.getrecord(True)

#when in dictionary from
for x in range(len(record)):
    lights, cars = record[x]
    print(f"t = {x} : {lights}")
    for lane in cars.keys():
        for car in cars[lane]:
            print(f"t = {x} {lane} : {car}")

#when in list from
for x in range(len(record)):
    lights, cars = record[x]
    print(f"t = {x} : {lights}")
    for car in cars:
        print(f"t = {x} : {car}")