from libs import *

inter = Intersection()

for x in [5, 10, 22]:
    inter.addcar(
        position = [x, 60],
        velocity = randint(1, 4)
    )


for x in [7, 11, 25]:
    inter.addcar(
        position = [60, x],
        velocity = randint(1, 4)
    )

for x in [7, 11, 25]:
    inter.addcar(
        position = [60, 60 + x],
        velocity = randint(1, 4)
    )

for x in [7, 11, 25]:
    inter.addcar(
        position = [60 + x, 60],
        velocity = randint(1, 4)
    )

inter.lightstate['left'] = GREEN

print(inter)

for i in range(19) : inter.updateframe()

print(inter)
print()

inter.updateframe()

print(inter)
inter.printcars()