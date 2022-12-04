from pull2021 import AocInteraction


#  https://adventofcode.com/2021/day/8

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        count = 0
        for line in input_file:
            line_split = line.strip().split("|")
            notes = [set(list(x)) for x in line_split[1].split(" ")]
            for n in notes:
                if len(n) in [2, 3, 4, 7]:
                    count += 1

        advent_of_code.answer(1, count)


#  aaa
# b    c
#  ddd
# e    f
#  ggg
def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        count = 0
        for line in input_file:
            line_split = line.strip().split("|")
            signals = [set(list(x)) for x in line_split[0].split(" ")]
            output = [set(list(x)) for x in line_split[1].split(" ")]
            signal_map = {}
            m = {}
            for n in signals:
                if len(n) == 2:
                    m[1] = n
                elif len(n) == 3:
                    m[7] = n
                elif len(n) == 4:
                    m[4] = n
                elif len(n) == 7:
                    m[8] = n
            signal_map['a'] = m[7].difference(m[1]).pop()

            # find 6
            for n in signals:
                n_diff = m[8].difference(n)
                if len(n_diff) == 1 and n_diff.pop() in m[1]:
                    m[6] = n
                    signal_map['c'] = m[6].difference(m[1]).pop()
            # find 5
            for n in signals:
                n_diff = m[6].difference(n)
                if len(n) == 5 and len(n_diff) == 1:
                    x = n_diff.pop()
                    if x not in m[1]:
                        m[5] = n
                        signal_map['e'] = x

            m[9] = m[5].union(m[4])
            signal_map['g'] = m[5].difference(m[4]).difference(m[7]).pop()
            # find 3
            for n in signals:
                if len(n) == 5 and signal_map['e'] in n:
                    m[2] = n
                    m[3] = n.copy()
                    m[3].remove(signal_map['e'])
                    m[3] = m[3].union(m[1])
                    m[0] = m[8].difference(m[3]).union(m[7]).union(set(signal_map['g']))
                    break

            result = 0

            for j in range(0, len(output)):
                for i in range(0, 10):
                    if output[j] == m[i]:
                        result += i * pow(10, len(output) - j - 1)
            count += result

        advent_of_code.answer(2, count)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
