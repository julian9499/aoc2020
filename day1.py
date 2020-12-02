numberArr = []
f = open("inputs/input_day1.txt", "r")
for line in f:
    numberArr.append(int(line))

for i in range(len(numberArr)):
    for j in range(i, len(numberArr)):
        for k in range(j, len(numberArr)):
            if numberArr[i] + numberArr[j] + numberArr[k] == 2020:
                print numberArr[i] * numberArr[j] * numberArr[k]
