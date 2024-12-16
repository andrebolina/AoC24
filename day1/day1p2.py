fileName = "input.txt"

leftList = []
rightList = []
similarityScore = 0

with open(fileName) as file:
    while line := file.readline():
        ids = line.rstrip().split()
        leftList.append(ids[0])
        rightList.append(ids[1])

for idValue in leftList:
    idCount = rightList.count(idValue)
    similarityScore += int(idValue) * idCount

print(similarityScore)