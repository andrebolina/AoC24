fileName = "input.txt"

leftList = []
rightList = []
totalDistance = 0

with open(fileName) as file:
    while line := file.readline():
        ids = line.rstrip().split()
        leftList.append(ids[0])
        rightList.append(ids[1])

leftList.sort()
rightList.sort()

for position in range(len(leftList)):
    leftId = int(leftList[position])
    rightId = int(rightList[position])
    totalDistance += leftId - rightId if leftId > rightId else rightId - leftId

print(totalDistance)