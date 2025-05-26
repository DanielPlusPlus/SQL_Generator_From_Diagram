class ConnectionModel:
    def __init__(self, FirstTable, SecondTable):
        self.FirstTable = FirstTable
        self.SecondTable = SecondTable

    def getFirstTable(self):
        return self.FirstTable

    def getSecondTable(self):
        return self.SecondTable
