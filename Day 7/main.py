from pull import AocInteraction


#  https://adventofcode.com/2022/day/7

class Dir:
    def __init__(self, name, parentDir):
        self.name = name
        self.parentDir = parentDir
        self.files = []
        self.dirs = []

    def getDirByName(self, dirName):
        if self.name == dirName:
            return self

        for d in self.dirs:
            if d.name == dirName:
                return d

        for d in self.dirs:
            FoundDir = d.getDirByName(dirName)
            if FoundDir is not None and FoundDir.name == dirName:
                return FoundDir

    def getChildDir(self, dirName):
        for d in self.dirs:
            if d.name == dirName:
                return d

    def print(self, tabs):
        print(tabs + self.name)
        for x in self.dirs:
            x.print(tabs + " ")

    def setDir(self, files, dirs):
        self.files = files
        self.dirs = dirs

    def getDirSize(self):
        size = sum(self.files)
        for x in self.dirs:
            size += x.getDirSize()
        return size

    def getAllDirs(self):
        l = self.dirs.copy()
        for x in self.dirs:
            if x.getAllDirs() is not None:
                for i in x.getAllDirs():
                    l.append(i)
        return l

    def setParentDir(self, parentDir):
        self.parentDir = parentDir

    def addFile(self, file):
        self.files.append(file)

    def addDir(self, dir):
        self.dirs.append(dir)



def part_1(advent_of_code, file_as_string_array):
    headDir = getHeadDir(file_as_string_array)

    s = 0
    for x in headDir.getAllDirs():
        if x.getDirSize() < 100000:
            s += x.getDirSize()

    advent_of_code.answer(1, s)

def getHeadDir(file_as_string_array):
    headDir = Dir("/", None)
    headDir.setParentDir(headDir)
    curDir = headDir
    for line in file_as_string_array:
        commands = line.split(" ")
        if commands[0] == "$":
            if commands[1] == "cd":
                if commands[2] == "..":
                    curDir = curDir.parentDir
                elif commands[2] == "/":
                    curDir = headDir
                else:
                    curDir = curDir.getChildDir(commands[2])


        elif commands[0] == "dir":
            curDir.addDir(Dir(commands[1], curDir))
        else:
            curDir.addFile(int(commands[0]))
    return headDir


def part_2(advent_of_code, file_as_string_array):
    headDir = getHeadDir(file_as_string_array)

    total_space_left = 70000000 - headDir.getDirSize()

    s = 100000000000
    for x in headDir.getAllDirs():
        if x.getDirSize() + total_space_left >= 30000000 and x.getDirSize() < s:
            s = x.getDirSize()
            print(x.name)

    advent_of_code.answer(2, s)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
