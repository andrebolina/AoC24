fileName = "input.txt"

totalSafeReports = 0

def isSafe(levels):
    singleBadLevelFound = False
    behavior = "increasing" if int(levels[0]) < int(levels[1]) else "decreasing"
    for position in range(len(levels) - 1):
        firstPosition = int(levels[position])
        secondPosition = int(levels[position + 1])

        if (firstPosition > secondPosition and behavior == "increasing") or (firstPosition < secondPosition and behavior == "decreasing"):
            if singleBadLevelFound:
                return False
            
            singleBadLevelFound = True
            continue
            

        diff = firstPosition - secondPosition
        if diff == 0 or diff < -3 or diff > 3:
            if singleBadLevelFound:
                return False
            
            singleBadLevelFound = True
            continue

    return True

with open(fileName) as file:
    while line := file.readline():
        levels = line.rstrip().split()
        if (isSafe(levels)):
            totalSafeReports += 1

print(totalSafeReports)