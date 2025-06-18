class ConnectionModel:
    def __init__(self, FirstTable, SecondTable, firstSelectedColumnName, secondSelectedColumnName):
        self.FirstTable = FirstTable
        self.SecondTable = SecondTable
        self.firstSelectedColumnName = firstSelectedColumnName
        self.secondSelectedColumnName = secondSelectedColumnName

    def getFirstTable(self):
        return self.FirstTable

    def getSecondTable(self):
        return self.SecondTable

    def getFirstSelectedColumnName(self):
        return self.firstSelectedColumnName

    def getSecondSelectedColumnName(self):
        return self.secondSelectedColumnName

    # do poprawy
    def contains(self, point, threshold=5):
        start = self.FirstTable.getRectangle().center()
        end = self.SecondTable.getRectangle().center()

        dx = end.x() - start.x()
        dy = end.y() - start.y()

        if dx == 0 and dy == 0:
            return (start - point).manhattanLength() <= threshold

        t = ((point.x() - start.x()) * dx + (point.y() - start.y()) * dy) / (dx * dx + dy * dy)
        t = max(0, min(1, t))

        closest_x = start.x() + t * dx
        closest_y = start.y() + t * dy

        dist = ((closest_x - point.x()) ** 2 + (closest_y - point.y()) ** 2) ** 0.5
        return dist <= threshold
