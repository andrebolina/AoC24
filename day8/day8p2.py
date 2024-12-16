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
                        if not [ (a,b) for a, b in antinodesPositions if a == x and b == y ]:
                            antinodesPositions.append((x, y))
                            totalAntinodes += 1

                        xDif = 0
                        yDif = 0
                        xPos = -1
                        yPos = -1

                        if x > i and (x + (x - i)) < maxHeight:
                            xDif = x - i
                            xPos = x + xDif
                        elif x < i and (x - (i - x)) >= 0:
                            xDif = (i - x) * -1
                            xPos = x + xDif

                        if y > j and (y + (y - j)) < maxWidth:
                            yDif = y - j
                            yPos = y + yDif
                        elif y < j and (y - (j - y)) >= 0:
                            yDif = (j - y) * -1
                            yPos = y + yDif
                        

                        while xPos >= 0 and yPos >= 0 and xPos < maxHeight and yPos < maxWidth:
                            if not [ (a,b) for a, b in antinodesPositions if a == xPos and b == yPos ]:
                                antinodesPositions.append((xPos, yPos))
                                totalAntinodes += 1
                            
                            xPos += xDif
                            yPos += yDif

print(totalAntinodes)