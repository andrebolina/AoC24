import re 

fileName = "input.txt"

def isXmas(firstLine, thirdLine):
    if firstLine[0] == "M" and firstLine[2] == "S" and thirdLine[0] == "M" and thirdLine[2] == "S":
        return True

    if firstLine[0] == "M" and firstLine[2] == "M" and thirdLine[0] == "S" and thirdLine[2] == "S":
        return True

    if firstLine[0] == "S" and firstLine[2] == "M" and thirdLine[0] == "S" and thirdLine[2] == "M":
        return True

    if firstLine[0] == "S" and firstLine[2] == "S" and thirdLine[0] == "M" and thirdLine[2] == "M":
        return True
    
    return False

totalXMAS = 0

table = []

with open(fileName) as file:
    while line := file.readline():
        table.append(line.rstrip())

totalWidth = len(table[0])
totalHeight = len(table)

for i in range(totalHeight):
    for j in range(totalWidth):
        if table[i][j] == "A" and i > 0 and i < totalHeight-1 and j > 0 and j < totalWidth-1 and isXmas(table[i-1][j-1:j+2], table[i+1][j-1:j+2]):
            totalXMAS += 1


print(totalXMAS)