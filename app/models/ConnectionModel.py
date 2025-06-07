class ConnectionModel:
    def __init__(self, FirstTable, SecondTable, FirstSelectedColumn, SecondSelectedColumn):
        self.FirstTable = FirstTable
        self.SecondTable = SecondTable
        self.FirstSelectedColumn = FirstSelectedColumn
        self.SecondSelectedColumn = SecondSelectedColumn

    def getFirstTable(self):
        return self.FirstTable

    def getSecondTable(self):
        return self.SecondTable

    def getFirstSelectedColumn(self):
        return self.FirstSelectedColumn

    def getSecondSelectedColumn(self):
        return self.SecondSelectedColumn
