fileName = "input.txt"

filesystem = []
filesystemChecksum = 0
checkedValues = []

with open(fileName) as file:
    line = file.readline()
    values = list(line.rstrip())

    idCont = 0
    for i in range(len(values)):
        value = int(values[i])
        if i % 2 == 0:
            for j in range(value):
                filesystem.append(str(idCont))
            idCont += 1
        else:
            for j in range(value):
                filesystem.append(".")

totalPos = len(filesystem)
lastOfValueIndex = totalPos
while lastOfValueIndex > 0:
    lastOfValueIndex -= 1
    value = filesystem[lastOfValueIndex]
    if value != "." and value not in checkedValues:
        checkedValues.append(value)
        firstOfValueIndex = lastOfValueIndex
        while filesystem[firstOfValueIndex] == value:
            firstOfValueIndex -= 1

        firstOfValueIndex += 1
        valuePositions = (lastOfValueIndex - firstOfValueIndex) + 1
        lastOfValueIndex = firstOfValueIndex

        firstFreePosIndex = filesystem.index(".")
        while firstFreePosIndex < lastOfValueIndex:
            if filesystem[firstFreePosIndex] == ".":
                lastFreePosIndex = firstFreePosIndex
                while lastFreePosIndex < totalPos and filesystem[lastFreePosIndex] == ".":
                    lastFreePosIndex += 1
                
                lastFreePosIndex -= 1
                freePositions = (lastFreePosIndex - firstFreePosIndex) + 1

                if (freePositions >= valuePositions):
                    for x in range(valuePositions):
                        filesystem.pop(firstFreePosIndex + x)
                        filesystem.insert(firstFreePosIndex + x, value)
                        filesystem.pop(firstOfValueIndex + x)
                        filesystem.insert(firstOfValueIndex + x, ".")

                    lastFreePosIndex = totalPos

                firstFreePosIndex = lastFreePosIndex + 1
            else:
                firstFreePosIndex += 1

for i in range(totalPos):
    if (filesystem[i] != "."):
        filesystemChecksum += int(filesystem[i]) * i

print(filesystemChecksum)