from app.models.ConnectionModel import ConnectionModel


class InheritanceModel(ConnectionModel):
    def __init__(self, FirstTable, SecondTable, FirstSelectedColumn, SecondSelectedColumn):
        super().__init__(FirstTable, SecondTable, FirstSelectedColumn, SecondSelectedColumn)
