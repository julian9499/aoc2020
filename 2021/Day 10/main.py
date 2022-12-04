from pull2021 import AocInteraction

#  https://adventofcode.com/2021/day/10
m = {')': 3, ']': 57, '}': 1197, '>': 25137}

get_close = {'(': ')', '[': ']', '{': '}', '<': '>'}

m2 = {')': 1, ']': 2, '}': 3, '>': 4}

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        errors = []
        for line in input_file:
            line_list = list(line.strip())
            stack = []
            for c in line_list:
                if c in ['(', '[', '{', '<']:
                    stack.append(c)
                elif c in [')', ']', '}', '>']:
                    close = get_close[stack.pop()]
                    if close != c:
                        errors.append(c)
                        break
        ans = sum([m[c] for c in errors])

        advent_of_code.answer(1, ans)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        scores = []
        for line in input_file:
            line_list = list(line.strip())
            stack = []
            err = False
            for c in line_list:
                if c in ['(', '[', '{', '<']:
                    stack.append(c)
                elif c in [')', ']', '}', '>']:
                    close = get_close[stack.pop()]
                    if close != c:
                        err = True
                        break
            if not(err):
                stack.reverse()
                seq = [get_close[x] for x in stack]
                count = 0
                for s in seq:
                    count = count * 5 + m2[s]
                scores.append(count)
        scores.sort()

        advent_of_code.answer(2, scores[int(len(scores)/2)])


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
