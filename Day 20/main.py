from pull import AocInteraction


#  https://adventofcode.com/2022/day/20

def part_1(advent_of_code, file_as_string_array):
    numbers = [{"number": int(file_as_string_array[x]), "org_index": x} for x in range(0, len(file_as_string_array))]
    for n in range(0, len(numbers)):
        for n_index in range(0, len(numbers)):
            if numbers[n_index]["org_index"] == n:
                # newindex = n_index + numbers[n_index]["number"]
                # # if newindex < 0:
                # #     newindex = len(numbers) - n_index + numbers[n_index]["number"]
                temp = numbers[n_index]
                # # if newindex >= n_index:
                # #     newindex += 1
                # if newindex > 0:
                #     newindex = newindex % len(numbers)
                # numbers.remove(temp)
                # numbers.insert(newindex, temp)
                # #
                extraRange = 0
                if n_index + numbers[n_index]["number"] < 0:
                    extraRange = -1
                elif n_index + numbers[n_index]["number"] >= len(numbers):
                    extraRange = 1
                if numbers[n_index]["number"] < 0:
                    for i in range(0, numbers[n_index]["number"] + extraRange, -1):
                        if n_index + i == 0:
                            numbers.append(numbers[0])
                            numbers = numbers[1:]
                        else:
                            swap(numbers, (n_index + i ) % -len(numbers), (n_index + i - 1) % -len(numbers))

                else:
                    for i in range(0, numbers[n_index]["number"] + extraRange):
                        if n_index + i == len(numbers):
                            numbers.insert(0, numbers[n_index + i -1])
                            numbers = numbers[:-1]
                        else:
                            swap(numbers, (n_index + i) % len(numbers), (n_index + i + 1) % len(numbers))
                # print([x["number"] for x in numbers], temp["number"])
                break
    # print([x["number"] for x in numbers])
    coord = 0
    for i in range(0, len(numbers)):
        if numbers[i]["number"] == 0:
            coord = i
            break
    print(sum([numbers[(coord+1000) % len(numbers)]["number"], numbers[(coord+2000)% len(numbers)]["number"], numbers[(coord+3000)% len(numbers)]["number"]]))
    print(numbers[(coord+1000) % len(numbers)]["number"], numbers[(coord+2000)% len(numbers)]["number"], numbers[(coord+3000)% len(numbers)]["number"])
    advent_of_code.answer(1, sum([numbers[(coord+1000) % len(numbers)]["number"], numbers[(coord+2000)% len(numbers)]["number"], numbers[(coord+3000)% len(numbers)]["number"]]))


def swap(l, ind1, ind2):
    temp = l[ind1]
    l[ind1] = l[ind2]
    l[ind2] = temp


def part_2(advent_of_code, file_as_string_array):
    numbers = [{"number": int(file_as_string_array[x]) * 811589153, "org_index": x} for x in range(0, len(file_as_string_array))]
    for k in range(0, 10):
        print(k)
        for n in range(0, len(numbers)):
            for n_index in range(0, len(numbers)):
                if numbers[n_index]["org_index"] == n:
                    numb = 0
                    if numbers[n_index]["number"] > 0:
                        numb = numbers[n_index]["number"] % (len(numbers) - 1)
                    else:
                        numb = numbers[n_index]["number"] % (-len(numbers) + 1)
                    extraRange = 0
                    if n_index + numb < 0:
                        extraRange = -1
                    elif n_index + numb >= len(numbers):
                        extraRange = 1
                    if numb < 0:
                        for i in range(0, numb + extraRange, -1):
                            if n_index + i == 0:
                                numbers.append(numbers[0])
                                numbers = numbers[1:]
                            else:
                                swap(numbers, (n_index + i) % -len(numbers), (n_index + i - 1) % -len(numbers))

                    else:
                        for i in range(0, numb +extraRange):
                            if n_index + i == len(numbers):
                                numbers.insert(0, numbers[n_index + i - 1])
                                numbers = numbers[:-1]
                            else:
                                swap(numbers, (n_index + i) % len(numbers), (n_index + i + 1) % len(numbers))
                    break
    coord = 0
    for i in range(0, len(numbers)):
        if numbers[i]["number"] == 0:
            coord = i
            break
    print(sum([numbers[(coord + 1000) % len(numbers)]["number"], numbers[(coord + 2000) % len(numbers)]["number"],
               numbers[(coord + 3000) % len(numbers)]["number"]]))
    print(numbers[(coord + 1000) % len(numbers)]["number"], numbers[(coord + 2000) % len(numbers)]["number"],
          numbers[(coord + 3000) % len(numbers)]["number"])
    advent_of_code.answer(2, sum([numbers[(coord + 1000) % len(numbers)]["number"],
                                  numbers[(coord + 2000) % len(numbers)]["number"],
                                  numbers[(coord + 3000) % len(numbers)]["number"]]))


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    # part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
