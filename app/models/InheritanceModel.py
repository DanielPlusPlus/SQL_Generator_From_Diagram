from app.models.ConnectionModel import ConnectionModel


class InheritanceModel(ConnectionModel):
    def __init__(self, FirstTable, SecondTable, firstSelectedColumnName, secondSelectedColumnName):
        super().__init__(FirstTable, SecondTable, firstSelectedColumnName, secondSelectedColumnName)
