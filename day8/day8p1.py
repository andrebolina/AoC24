fileName = "input.txt"

totalAntinodes = 0
antinodesPositions = []
cityMap = []

with open(fileName) as file:
    while line := file.readline():
        cityMap.append(list(line.rstrip()))

maxHeight = len(cityMap)
maxWidth = len(cityMap[0])

for i in range(maxHeight):
    for j in range(maxWidth):
        if cityMap[i][j] != ".":
            signal = cityMap[i][j]
            for x in range(maxHeight):
                for y in range(maxWidth):
                    if (x != i or y != j) and cityMap[x][y] == signal:
                        xPos = -1
                        yPos = -1

                        if x > i and (x + (x - i)) < maxHeight:
                            xPos = (x + (x - i))
                        elif x < i and (x - (i - x)) >= 0:
                            xPos = (x - (i - x))

                        if y > j and (y + (y - j)) < maxWidth:
                            yPos = (y + (y - j))
                        elif y < j and (y - (j - y)) >= 0:
                            yPos = (y - (j - y))
                        

                        if xPos >= 0 and yPos >= 0 and not [ (a,b) for a, b in antinodesPositions if a == xPos and b == yPos ]:
                            antinodesPositions.append((xPos, yPos))
                            totalAntinodes += 1

print(totalAntinodes)