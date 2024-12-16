class MySolution:
    fileName = "input.txt"

    totalPrice = 0
    totalHeight = 0
    totalWidth = 0
    regionsMap = []
    visitedPositions = []

    def __init__(self):
        with open(self.fileName) as file:
            while line := file.readline():
                self.regionsMap.append(list(line.rstrip()))

        self.totalHeight = len(self.regionsMap)
        self.totalWidth = len(self.regionsMap[0])

    def result(self):
        for i in range(self.totalHeight):
            for j in range(self.totalWidth):
                area, perimeter = self.calculateRegion(self.regionsMap[i][j], i, j)
                self.totalPrice += area * perimeter

        return self.totalPrice

    def calculateRegion(self, plant, posY, posX):
        if [(a,b) for a, b in self.visitedPositions if a == posY and b == posX]:
            return 0, 0

        self.visitedPositions.append((posY, posX))

        perimeter = 4
        area = 1

        if posY > 0 and self.regionsMap[posY-1][posX] == plant and not [(a,b) for a, b in self.visitedPositions if a == posY-1 and b == posX]:
            subArea, subPerimeter = self.calculateRegion(plant, posY-1, posX)
            area += subArea
            perimeter += subPerimeter
        if posX > 0 and self.regionsMap[posY][posX-1] == plant and not [(a,b) for a, b in self.visitedPositions if a == posY and b == posX-1]:
            subArea, subPerimeter = self.calculateRegion(plant, posY, posX-1)
            area += subArea
            perimeter += subPerimeter
        if posY+1 < self.totalHeight and self.regionsMap[posY+1][posX] == plant and not [(a,b) for a, b in self.visitedPositions if a == posY+1 and b == posX]:
            subArea, subPerimeter = self.calculateRegion(plant, posY+1, posX)
            area += subArea
            perimeter += subPerimeter
        if posX+1 < self.totalWidth and self.regionsMap[posY][posX+1] == plant and not [(a,b) for a, b in self.visitedPositions if a == posY and b == posX+1]:
            subArea, subPerimeter = self.calculateRegion(plant, posY, posX+1)
            area += subArea
            perimeter += subPerimeter

        if posY > 0 and self.regionsMap[posY-1][posX] == plant:
            perimeter -= 1
        if posX > 0 and self.regionsMap[posY][posX-1] == plant :
            perimeter -= 1
        if posY+1 < self.totalHeight and self.regionsMap[posY+1][posX] == plant:
            perimeter -= 1
        if posX+1 < self.totalWidth and self.regionsMap[posY][posX+1] == plant:
            perimeter -= 1

        return area, perimeter


if __name__ == "__main__":
    obj = MySolution()
    print(obj.result())