from pull import AocInteraction


def hasCardWon(numbers, card):
    for i in range(0, 5):
        if all(elem in numbers for elem in card[i]):
            return True
        if card[0][i] in numbers and card[1][i] in numbers and card[2][i] in numbers and card[3][i] in numbers and card[4][i] in numbers:
            return True
    return False

#  https://adventofcode.com/2021/day/4

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        bingonumbers = [int(x) for x in input_file.readline().replace("\n", "").split(",")]
        bingoCards = []
        bingoCard = []
        for line in input_file:
            if line == "\n" and len(bingoCard) !=5:
                continue
            elif line == "\n" and len(bingoCard) == 5:
                bingoCards.append(bingoCard)
                bingoCard = []
            else:
                bingoCard.append([int(x) for x in " ".join(line.replace("\n", "").split()).split(" ")])

        chosenNumbers = []
        winningCard = []
        stop = False
        for x in bingonumbers:
            chosenNumbers.append(x)
            for card in bingoCards:
                if hasCardWon(chosenNumbers, card):
                    winningCard = card
                    stop = True
            if stop:
                break


        sumOfNum = 0

        for x in winningCard:
            for y in x:
                if y not in chosenNumbers:
                    sumOfNum += y

        advent_of_code.answer(1,sumOfNum * chosenNumbers[len(chosenNumbers)-1])


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        bingonumbers = [int(x) for x in input_file.readline().replace("\n", "").split(",")]
        bingoCards = []
        bingoCard = []
        for line in input_file:
            if line == "\n" and len(bingoCard) !=5:
                continue
            elif line == "\n" and len(bingoCard) == 5:
                bingoCards.append(bingoCard)
                bingoCard = []
            else:
                bingoCard.append([int(x) for x in " ".join(line.replace("\n", "").split()).split(" ")])

        chosenNumbers = []
        winningCards = []
        lastWinningCard = None
        lastChosenNumberState = None
        for x in bingonumbers:
            chosenNumbers.append(x)
            for card in bingoCards:
                if hasCardWon(chosenNumbers, card):
                    winningCards.append(card)
            if len(winningCards) > 0:
                for k in winningCards:
                    bingoCards.remove(k)
                    lastWinningCard = k
                    lastChosenNumberState = chosenNumbers.copy()
                    winningCards = []


        sumOfNum = 0
        for x in lastWinningCard:
            for y in x:
                if y not in lastChosenNumberState:
                    sumOfNum += y

        advent_of_code.answer(2, sumOfNum * lastChosenNumberState[len(lastChosenNumberState)-1])


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
