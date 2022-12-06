from pull import AocInteraction


#  https://adventofcode.com/2022/day/6

def part_1(advent_of_code, file_as_string_array):
    signals = list(file_as_string_array[0])

    ans = 0
    for i in range(0, len(signals)-4):
        start_sig = set(signals[i:i+4])
        print(start_sig)
        if len(start_sig) == 4:
            ans = i+4
            break
    
    advent_of_code.answer(1, ans)


def part_2(advent_of_code, file_as_string_array):
    signals = list(file_as_string_array[0])

    ans = 0
    message_length = 14
    for i in range(0, len(signals) - message_length):
        start_sig = set(signals[i:i + message_length])
        print(start_sig)
        if len(start_sig) == message_length:
            ans = i + message_length
            break

    advent_of_code.answer(2, ans)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
