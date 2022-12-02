from pull2021 import AocInteraction



#  https://adventofcode.com/2021/day/6

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        state = map(int, input_file.readline().strip().split(","))
        for x in range(0, 80):
            newState = []
            for fish in state:
                if fish == 0:
                    newState.append(8)
                    newState.append(6)
                else:
                    newState.append(fish-1)
            state = newState
        # f = open("input_80days.txt", "w")
        # f.write(str(state))

        advent_of_code.answer(1, len(state))


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        state = list(map(int, input_file.readline().strip().split(",")))
        newBigState = [] # USE DYNAMIC PROGRAMMING
        count = 0
        for i in state:
            # localstate = [i]
            count += fish(256, 0, i)
            print(count)
            # print(count)
            # for x in range(0, 43):
            #     newState = []
            #     for fish in localstate:
            #         if fish == 0:
            #             newState.append(8)
            #             newState.append(6)
            #         else:
            #             newState.append(fish - 1)
            #     localstate = newState
            # for j in localstate:
            #     newBigState.append(j)

        # total = 0
        # print(len(newBigState))
        # for i in newBigState:
        #     localstate = [i]
        #     for x in range(0, 256-123):
        #         newState = []
        #         for fish in localstate:
        #             if fish == 0:
        #                 newState.append(8)
        #                 newState.append(6)
        #             else:
        #                 newState.append(fish - 1)
        #         localstate = newState
        #     # print(localstate)
        #     total += len(localstate)

        advent_of_code.answer(2, count)

def fish(days, init_time, initial_state):
    if init_time + initial_state >= days:
        return 1
    return fish(days, init_time+initial_state+1, 6) + fish(days, init_time+initial_state+1, 8)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
