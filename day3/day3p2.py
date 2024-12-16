import re 

fileName = "input.txt"

totalMultiplications = 0

with open(fileName) as file:
    mul_enabled = True

    while line := file.readline():
        mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        do_pattern = r'do\(\)'
        dont_pattern = r"don't\(\)"

        pos = 0
        while pos < len(line):
            mul_match = re.search(mul_pattern, line[pos:])
            do_match = re.search(do_pattern, line[pos:])
            dont_match = re.search(dont_pattern, line[pos:])

            if mul_match and (not do_match or mul_match.start() < do_match.start()) and (not dont_match or mul_match.start() < dont_match.start()):
                if mul_enabled:
                    x, y = mul_match.groups()
                    totalMultiplications += int(x) * int(y)
                pos += mul_match.end()
            elif do_match and (not dont_match or do_match.start() < dont_match.start()):
                mul_enabled = True
                pos += do_match.end()
            elif dont_match:
                mul_enabled = False
                pos += dont_match.end()
            else:
                pos = len(line)

print(totalMultiplications)