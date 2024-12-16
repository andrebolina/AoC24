import re 

fileName = "input.txt"

def isXmas(l1, l2, l3, l4):
    if l1 == "X" and l2 == "M" and l3 == "A" and l4 == "S":
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
        #check regular
        if totalWidth - j >= 4 and isXmas(table[i][j], table[i][j+1], table[i][j+2], table[i][j+3]):
            totalXMAS += 1

        #check backwards
        if j >= 3 and isXmas(table[i][j], table[i][j-1], table[i][j-2], table[i][j-3]):
            totalXMAS += 1

        #check vertical below
        if totalHeight - i >= 4 and isXmas(table[i][j], table[i+1][j], table[i+2][j], table[i+3][j]):
            totalXMAS += 1

        #check vertical above
        if i >= 3 and isXmas(table[i][j], table[i-1][j], table[i-2][j], table[i-3][j]):
            totalXMAS += 1

        #check diagonal right top
        if i >= 3 and totalWidth - j >= 4 and isXmas(table[i][j], table[i-1][j+1], table[i-2][j+2], table[i-3][j+3]):
            totalXMAS += 1

        #check diagonal right bottom
        if totalHeight - i >= 4 and totalWidth - j >= 4 and isXmas(table[i][j], table[i+1][j+1], table[i+2][j+2], table[i+3][j+3]):
            totalXMAS += 1

        #check diagonal left bottom
        if totalHeight - i >= 4 and j >= 3 and isXmas(table[i][j], table[i+1][j-1], table[i+2][j-2], table[i+3][j-3]):
            totalXMAS += 1

        #check diagonal left top
        if i >= 3 and j >= 3 and isXmas(table[i][j], table[i-1][j-1], table[i-2][j-2], table[i-3][j-3]):
            totalXMAS += 1

print(totalXMAS)