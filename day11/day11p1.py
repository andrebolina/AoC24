fileName = "input.txt"

blinks = 25
stones = []

with open(fileName) as file:
    line = file.readline()
    stones = line.rstrip().split(" ")

for blink in range(blinks):
    pos = 0
    while pos < len(stones):
        number = int(stones[pos])
        digits = len(stones[pos])
        if number == 0:
            stones[pos] = str(1)
        elif digits % 2 == 0:
            half = int(digits / 2)
            firstHalf = stones[pos][0:half]
            secondHalf = int(stones[pos][half:digits])
            stones[pos] = firstHalf
            stones.insert(pos + 1, str(secondHalf))
            pos += 1
        else:
            stones[pos] = str(number * 2024)

        pos += 1

print(len(stones))