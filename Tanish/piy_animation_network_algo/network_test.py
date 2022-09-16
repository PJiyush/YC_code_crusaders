from libs import *

t = 100
i = Intersection()
no_of_cars_in_a_lane = 5
i.spawncars(no_of_cars_in_a_lane)
algo = NetworkAlgorithm(i, thresh = 30)
algo.runsimulation(endtime = t, record=True)
timeline = algo.getrecord(True)

print(timeline)