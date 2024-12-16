import math

fileName = "input.txt"

orderRules = {}
updates = []
middlePageTotal = 0

with open(fileName) as file:
    while line := file.readline():
        if line.find("|") > 0:
            pages = line.rstrip().split("|")
            firstPage = pages[0]
            secondPage = pages[1]
            if firstPage in orderRules:
                orderRules[firstPage].append(secondPage)
            else:
                orderRules[firstPage] = [secondPage]
        elif line.find(",") > 0:
            pages = line.rstrip().split(",")
            updates.append(pages)

for i in range(len(updates)):
    validOrder = True
    pagesToUpdate = len(updates[i])
    for j in range(pagesToUpdate):
        pos = (pagesToUpdate-1) - j
        if pos > 0:
            while updates[i][pos] in orderRules and any(x in orderRules[updates[i][pos]] for x in updates[i][0:pos]):
                validOrder = False
                newPos = pos - 1
                while newPos > 0 and any(x in orderRules[updates[i][pos]] for x in updates[i][0:newPos]):
                    newPos -= 1

                value = updates[i][pos]
                updates[i].pop(pos)
                updates[i].insert(newPos,value)

    if not validOrder:
        middlePos = math.floor(pagesToUpdate/2)
        middlePageTotal += int(updates[i][middlePos])
    
print(middlePageTotal)