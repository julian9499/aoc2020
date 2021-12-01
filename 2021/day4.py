import re


def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class PassPort:
    def __init__(self):
        self.map = {}

    def addKey(self, mapKey, value):
        if self.validateKey(mapKey, value):
            self.map[mapKey] = value
        else:
            print(mapKey + " " + value)

    def validateKey(self, mapKey, value):
        if mapKey == "byr":
            return len(value) == 4 and 1920 <= int(value) <= 2004
        if mapKey == "iyr":
            return len(value) == 4 and 2010 <= int(value) <= 2020
        if mapKey == "eyr":
            return len(value) == 4 and 2020 <= int(value) <= 2030
        if mapKey == "hgt" and value[-2:] == "cm":
            return 150 <= int(value[:-2]) <= 193
        if mapKey == "hgt" and value[-2:] == "in":
            return 59 <= int(value[:-2]) <= 76
        if mapKey == "hcl" and value[0] == "#":
            return re.search("^0123456789abcdef", value.replace('#', '')) or True
        if mapKey == "ecl":
            return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if mapKey == "pid" and len(value) == 9:
            return representsInt(value)
        if mapKey == "cid":
            return True

    def isValid(self):
        return "byr" in self.map and "iyr" in self.map and "eyr" in self.map and "hgt" in self.map and "hcl" in self.map and "ecl" in self.map and "pid" in self.map


f = open("inputs/input_day4.txt", "r")
currPassPort = PassPort()
passports = []
for line in f:
    if line[0] == '\n':
        passports.append(currPassPort)
        currPassPort = PassPort()
        continue
    for keyVal in line.split(' '):
        key = keyVal.split(':')[0]
        val = keyVal.split(':')[1].replace('\n', '')
        currPassPort.addKey(key, val)

passports.append(currPassPort)
currPassPort = PassPort()

count = 0
for p in passports:
    if p.isValid():
        count = count + 1

print(count)
