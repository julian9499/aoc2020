rangeMin = []
rangeMax = []
letter = []
word = []


f = open("../inputs/input_day2.txt", "r")
for line in f:
    item = line.split(' ')
    rng = item[0].split('-')
    rangeMin.append(int(rng[0]))
    rangeMax.append(int(rng[1]))
    letter.append(item[1][0])
    word.append(item[2].replace('\n', ''))

count = 0

for i in range(len(word)):
    wordCount = word[i].count(letter[i])
    containsMin = rangeMin[i] - 1 < len(word[i]) and word[i][rangeMin[i]-1] == letter[i]
    containsMax = rangeMax[i] - 1 < len(word[i]) and word[i][rangeMax[i]-1] == letter[i]

    if containsMin and containsMax:
        continue
    elif containsMin and not containsMax:
        count = count + 1
    elif containsMax and not containsMin:
        count = count + 1


print count

