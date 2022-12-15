from pull import AocInteraction

monkeys = []


class Monkey:
    def __init__(self, items, operation, test, ifTrue, ifFalse):
        self.items = items
        self.operation = operation
        self.test = test
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse
        self.inspected = 0

    def inspect(self):
        for i in self.items:
            self.inspected += 1
            item = self.operation(i)
            if self.test(item):
                monkeys[self.ifTrue].receive(item)
                # print(f"item: {i} became {item} and is thrown to {self.ifTrue}")
            else:
                monkeys[self.ifFalse].receive(item)
                # print(f"item: {i} became {item} and is thrown to {self.ifFalse}")
        self.items = []

    def receive(self, item):
        self.items.append(item)


#  https://adventofcode.com/2022/day/11

def part_1(advent_of_code, file_as_string_array):
    monkeys.append(Monkey([93, 98], lambda old: int((old * 17) / 3), lambda i: i % 19 == 0, 5, 3))
    monkeys.append(Monkey([95, 72, 98, 82, 86], lambda old: int((old + 5) / 3), lambda i: i % 13 == 0, 7, 6))
    monkeys.append(Monkey([85, 62, 82, 86, 70, 65, 83, 76], lambda old: int((old + 8) / 3), lambda i: i % 5 == 0, 3, 0))
    monkeys.append(Monkey([86, 70, 71, 56], lambda old: int((old + 1) / 3), lambda i: i % 7 == 0, 4, 5))

    monkeys.append(Monkey([77, 71, 86, 52, 81, 67], lambda old: int((old + 4) / 3), lambda i: i % 17 == 0, 1, 6))
    monkeys.append(Monkey([89, 87, 60, 78, 54, 77, 98], lambda old: int((old * 7) / 3), lambda i: i % 2 == 0, 1, 4))
    monkeys.append(Monkey([69, 65, 63], lambda old: int((old + 6) / 3), lambda i: i % 3 == 0, 7, 2))
    monkeys.append(Monkey([89], lambda old: int((old * old) / 3), lambda i: i % 11 == 0, 0, 2))

    for i in range(0, 20):
        for m in monkeys:
            m.inspect()

    counts = []
    for m in monkeys:
        counts.append(m.inspected)
    counts.sort(reverse=True)
    print(counts[0] * counts[1])

    advent_of_code.answer(1, counts[0] * counts[1])


def part_2(advent_of_code, file_as_string_array):
    supermod = 19*13*5*7*17*2*3*11
    monkeys.append(Monkey([93, 98], lambda old: int((old * 17)) % supermod, lambda i: i % 19 == 0, 5, 3))
    monkeys.append(Monkey([95, 72, 98, 82, 86], lambda old: int((old + 5))% supermod, lambda i: i % 13 == 0, 7, 6))
    monkeys.append(Monkey([85, 62, 82, 86, 70, 65, 83, 76], lambda old: int((old + 8))% supermod, lambda i: i % 5 == 0, 3, 0))
    monkeys.append(Monkey([86, 70, 71, 56], lambda old: int((old + 1))% supermod, lambda i: i % 7 == 0, 4, 5))

    monkeys.append(Monkey([77, 71, 86, 52, 81, 67], lambda old: int((old + 4))% supermod, lambda i: i % 17 == 0, 1, 6))
    monkeys.append(Monkey([89, 87, 60, 78, 54, 77, 98], lambda old: int((old * 7))% supermod, lambda i: i % 2 == 0, 1, 4))
    monkeys.append(Monkey([69, 65, 63], lambda old: int((old + 6))% supermod, lambda i: i % 3 == 0, 7, 2))
    monkeys.append(Monkey([89], lambda old: int((old * old))% supermod, lambda i: i % 11 == 0, 0, 2))

    for i in range(0, 10000):
        print(i)
        for m in monkeys:
            m.inspect()

    counts = []
    for m in monkeys:
        counts.append(m.inspected)
    counts.sort(reverse=True)
    print(counts[0] * counts[1])

    advent_of_code.answer(2, counts[0] * counts[1])


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
