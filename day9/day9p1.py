fileName = "input.txt"

filesystem = []
filesystemChecksum = 0

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
for i in range(totalPos):
    valueIndex = totalPos - i - 1
    value = filesystem[valueIndex]
    if value != ".":
        freePositionIndex = filesystem.index(".")
        if freePositionIndex > valueIndex:
            break

        filesystem.pop(freePositionIndex)
        filesystem.insert(freePositionIndex, value)
        filesystem.pop(valueIndex)
        filesystem.insert(valueIndex, ".")

for i in range(totalPos):
    if (filesystem[i] == "."):
        break

    filesystemChecksum += int(filesystem[i]) * i

print(filesystemChecksum)