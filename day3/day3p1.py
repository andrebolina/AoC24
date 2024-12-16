import re 

fileName = "input.txt"

totalMultiplications = 0

def minha():
    with open(fileName) as file:
        while line := file.readline():
            lastStartingPos = 0

            while startingPos := line.find("mul(", lastStartingPos):
                if (startingPos < 0):
                    break
                
                lastStartingPos = startingPos + 1
                endPos = line.find(")", startingPos)
                params = line[startingPos+4:endPos]
                values = params.split(",")

                try:
                    totalMultiplications += int(values[0]) * int(values[1])
                except:
                    continue

with open(fileName) as file:
    while line := file.readline():
        pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        valid_instructions = re.findall(pattern, line)
        for x, y in valid_instructions:
            totalMultiplications += int(x) * int(y)

print(totalMultiplications)