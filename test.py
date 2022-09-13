from libs import *

i = Intersection()
i.green('right')
i.spawncars(12)
i.updateframe(10)

print(i)
i.printcars()

# cai = i.getcarsatintersection()
# for x in cai.keys():
#     print(f"{x}:\n{cai[x]}")
# print()
c = i.getcars()

newc = {
    'right' : c['right'],
    'down' : c['down'],
    'left' : c['left'],
}

print(NetworkAlgorithm.getpriority(newc))