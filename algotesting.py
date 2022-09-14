from libs import *

i = Intersection()

i.spawncars()

i.printcars()

runner = NetworkAlgorithm(i)

while True:
    print()
    i.printcars()
    print()
    i.updateframe()
    input("Enter to proceed: ")