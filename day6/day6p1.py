import math

fileName = "input.txt"

mappedArea = []
totalDistinctPositions = 0

with open(fileName) as file:
    while line := file.readline():
        mappedArea.append(line.rstrip())

totalWidth = len(mappedArea[0])
totalHeight = len(mappedArea)

positionY = 0
positionX = 0

for i in range (totalHeight):
    try:
        index = mappedArea[i].index("^")
        positionX = index
        positionY = i
        break
    except:
        continue

while 0 <= positionY < totalHeight and 0 <= positionX < totalWidth:
    cursor = mappedArea[positionY][positionX]
    match cursor:
        case  "^":
            nextPositionY = positionY - 1
            nextPositionX = positionX
        case  ">":
            nextPositionY = positionY
            nextPositionX = positionX + 1
        case  "v":
            nextPositionY = positionY + 1
            nextPositionX = positionX
        case  "<":
            nextPositionY = positionY
            nextPositionX = positionX - 1

    try:
        nextPlace = mappedArea[nextPositionY][nextPositionX]
        if nextPlace == "#":
            match cursor:
                case  "^":
                    newCursor = ">"
                case  ">":
                    newCursor = "v"
                case  "v":
                    newCursor = "<"
                case  "<":
                    newCursor = "^"
            
            currentLine = list(mappedArea[positionY])
            currentLine[positionX] = newCursor
            mappedArea[positionY] = ''.join(currentLine)
        else:
            if nextPlace != "X":
                totalDistinctPositions += 1

            currentLine = list(mappedArea[positionY])
            currentLine[positionX] = "X"
            mappedArea[positionY] = ''.join(currentLine)

            nextLine = list(mappedArea[nextPositionY])
            nextLine[nextPositionX] = cursor
            mappedArea[nextPositionY] = ''.join(nextLine)

            positionY = nextPositionY
            positionX = nextPositionX
    except:
        break

print(totalDistinctPositions + 1)