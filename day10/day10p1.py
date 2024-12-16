class MySolution:
    fileName = "sample.txt"

    topographicMap = []
    totalHeight = 0
    totalWidth = 0
    trailheadPositions = []
    trailheadsScoresSum = 0


    def __init__(self):
        with open(self.fileName) as file:
            while line := file.readline():
                self.topographicMap.append(list(line.rstrip()))

        self.totalHeight = len(self.topographicMap)
        self.totalWidth = len(self.topographicMap[0])


    def result(self):
        for i in range(self.totalHeight):
            for j in range(self.totalWidth):
                if self.topographicMap[i][j] == "0":
                    self.trailheadPositions = []
                    self.trailheadsScoresSum += self.hikingTrails(int(self.topographicMap[i][j]), i, j)

        return self.trailheadsScoresSum


    def hikingTrails(self, value, posY, posX):
        if value == 9:
            if [ (a,b) for a, b in self.trailheadPositions if a == posY and b == posX ]:
                return 0
            else:
                self.trailheadPositions.append((posY, posX))
                return 1
        
        hikingTrailsScore = 0
        if (posX + 1 < self.totalWidth) and (value + 1 == int(self.topographicMap[posY][posX + 1])):
            hikingTrailsScore += self.hikingTrails(int(self.topographicMap[posY][posX + 1]), posY, posX + 1)
        if (posY + 1 < self.totalHeight) and (value + 1 == int(self.topographicMap[posY + 1][posX])):
            hikingTrailsScore += self.hikingTrails(int(self.topographicMap[posY + 1][posX]), posY + 1, posX)
        if (posX - 1 >= 0) and (value + 1 == int(self.topographicMap[posY][posX - 1])):
            hikingTrailsScore += self.hikingTrails(int(self.topographicMap[posY][posX - 1]), posY, posX - 1)
        if (posY - 1 >= 0) and (value + 1 == int(self.topographicMap[posY - 1][posX])):
            hikingTrailsScore += self.hikingTrails(int(self.topographicMap[posY - 1][posX]), posY - 1, posX)

        return hikingTrailsScore

if __name__ == "__main__":
    obj = MySolution()
    print(obj.result())