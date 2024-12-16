import re

class MySolution:
    fileName = "input.txt"

    robots = {}
    bathroomMap = []
    maxX = 103
    maxY = 101
    seconds = 100

    def __init__(self):
        with open(self.fileName) as file:
            id = 1
            while line := file.readline().rstrip():
                data = re.findall(r'(-?[\d]+)', line)
                self.robots[id] = {"posY": int(data[0]), "posX": int(data[1]), "velY": int(data[2]), "velX": int(data[3])}
                id += 1

        for x in range(self.maxX):
            line = []
            for y in range(self.maxY):
                line.append(0)
            
            self.bathroomMap.append(line)

        for _, props in self.robots.items():
            self.bathroomMap[props["posX"]][props["posY"]] = self.bathroomMap[props["posX"]][props["posY"]] + 1

    def movement(self):
        for id, props in self.robots.items():
            posX = props["posX"]
            posY = props["posY"]
            newPosX = posX + props["velX"]
            newPosY = posY + props["velY"]

            if newPosX < 0:
                newPosX = self.maxX + newPosX
            if newPosX >= self.maxX:
                newPosX = newPosX - self.maxX
            if newPosY < 0:
                newPosY = self.maxY + newPosY
            if newPosY >= self.maxY:
                newPosY = newPosY - self.maxY

            self.bathroomMap[posX][posY] = self.bathroomMap[posX][posY] - 1
            self.bathroomMap[newPosX][newPosY] = self.bathroomMap[newPosX][newPosY] + 1
            self.robots[id] = {"posY": newPosY, "posX": newPosX, "velX": props["velX"], "velY": props["velY"]}
                

    def result(self):
        for sec in range(self.seconds):
            self.movement()

        halfX = self.maxX // 2
        halfY = self.maxY // 2

        q1 = 0
        for i in range(halfX):
            for j in range(halfY):
                q1 += self.bathroomMap[i][j]

        q2 = 0
        for i in range(halfX):
            for j in range(halfY + 1, self.maxY):
                q2 += self.bathroomMap[i][j]

        q3 = 0
        for i in range(halfX + 1, self.maxX):
            for j in range(self.maxY // 2):
                q3 += self.bathroomMap[i][j]

        q4 = 0
        for i in range(halfX + 1, self.maxX):
            for j in range(halfY + 1, self.maxY):
                q4 += self.bathroomMap[i][j]

        return q1 * q2 * q3 * q4

    def print(self):
        for x in range(self.maxX):
            for y in range(self.maxY):
                print(self.bathroomMap[x][y], end="")

            print("")

if __name__ == "__main__":
    obj = MySolution()
    print(obj.result())