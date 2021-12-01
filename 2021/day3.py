class Travel:
    def __init__(self, map):
        self.xLocal = 0
        self.yLocal = 0
        self.map = map
        self.count = 0

    def setStep(self, x, y):
        self.xLocal = self.xLocal + x
        self.yLocal = (self.yLocal + y) % 31
        if self.xLocal >= len(self.map):
            self.count = self.count + 0
            return
        if self.map[self.xLocal][self.yLocal] == '#':
            self.count = self.count + 1

    def calcTrees(self, xTravel, yTravel):
        while self.xLocal < len(self.map):
            self.setStep(xTravel, yTravel)
        return self.count

map = []

f = open("../inputs/input_day3.txt", "r")
for line in f:
    treeLine = []
    for coord in line.replace('\n', ''):
        treeLine.append(coord)
    map.append(treeLine)

t1 = Travel(map).calcTrees(1, 1)
t2 = Travel(map).calcTrees(1, 3)
t3 = Travel(map).calcTrees(1, 5)
t4 = Travel(map).calcTrees(1, 7)
t5 = Travel(map).calcTrees(2, 1)

print(t1 * t2 * t3 * t4 * t5)



