from code import interact
from libs import *
file = open('file.txt','w')

i = Intersection()
i.spawncars(10)

algo = SimpleCycle(i,period=60)
algo.runsimulation()
x = algo.getrecord()
print(x)
for i in x:
    y = ' '.join(i)
    file.write(y)
# print(y)
file.close()