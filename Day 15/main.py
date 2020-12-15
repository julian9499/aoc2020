from pull import AocInteraction


#  https://adventofcode.com/2020/day/15

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        nums = [int(x) for x in input_file.readlines()[0].strip().split(",")]
        turn = 1
        last_spoken = {}
        nums_spoken = {}
        last_num = 0
        for i in nums:
            if i not in nums_spoken:
                nums_spoken[i] = 0
            if i not in last_spoken:
                last_spoken[i] = []
            last_spoken[i].append(turn)
            nums_spoken[i] += 1
            last_num = i
            turn += 1

        sumSpoken = sum(nums_spoken.values())
        while sumSpoken < 2020:
            if last_num in nums_spoken and nums_spoken[last_num] == 1:
                if 0 not in nums_spoken:
                    nums_spoken[0] = 0
                if 0 not in last_spoken:
                    last_spoken[0] = []
                last_spoken[0].append(turn)
                nums_spoken[0] += 1
                last_num = 0
            elif last_num in nums_spoken and nums_spoken[last_num] > 1:
                last_spoken[last_num].sort()
                ls = last_spoken[last_num][len(last_spoken[last_num])-2]
                last_spoken[last_num] = last_spoken[last_num][-2:]
                num = turn - 1 - ls
                if num not in nums_spoken:
                    nums_spoken[num] = 0
                if num not in last_spoken:
                    last_spoken[num] = []
                last_spoken[num].append(turn)
                nums_spoken[num] += 1
                last_num = num
            sumSpoken += 1
            # print(last_num)
            turn += 1

        advent_of_code.answer(1, last_num)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        nums = [int(x) for x in input_file.readlines()[0].strip().split(",")]
        turn = 1
        last_spoken = {}
        nums_spoken = {}
        last_num = 0
        for i in nums:
            if i not in nums_spoken:
                nums_spoken[i] = 0
            if i not in last_spoken:
                last_spoken[i] = []
            last_spoken[i].append(turn)
            nums_spoken[i] += 1
            last_num = i
            turn += 1

        sumSpoken = sum(nums_spoken.values())
        while sumSpoken < 30000000:
            if last_num in nums_spoken and nums_spoken[last_num] == 1:
                if 0 not in nums_spoken:
                    nums_spoken[0] = 0
                if 0 not in last_spoken:
                    last_spoken[0] = []
                last_spoken[0].append(turn)
                nums_spoken[0] += 1
                last_num = 0
            elif last_num in nums_spoken and nums_spoken[last_num] > 1:
                last_spoken[last_num].sort()
                ls = last_spoken[last_num][len(last_spoken[last_num])-2]
                last_spoken[last_num] = last_spoken[last_num][-2:]
                num = turn - 1 - ls
                if num not in nums_spoken:
                    nums_spoken[num] = 0
                if num not in last_spoken:
                    last_spoken[num] = []
                last_spoken[num].append(turn)
                nums_spoken[num] += 1
                last_num = num
            sumSpoken += 1
            turn += 1
        advent_of_code.answer(2, last_num)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
