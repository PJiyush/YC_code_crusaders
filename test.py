from libs import *

i = Intersection()
i.spawncars(3)
algo = NetworkAlgorithm(i)

algo.runsimulation(50)