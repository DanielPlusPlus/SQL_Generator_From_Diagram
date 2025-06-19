from app.models.ConnectionModel import ConnectionModel


class RelationshipModel(ConnectionModel):
    def __init__(self, FirstTable, SecondTable, firstSelectedColumnName, secondSelectedColumnName, relationshipType):
        super().__init__(FirstTable, SecondTable)
        self.firstSelectedColumnName = firstSelectedColumnName
        self.secondSelectedColumnName = secondSelectedColumnName
        self.relationshipType = relationshipType

    def getFirstSelectedColumnName(self):
        return self.firstSelectedColumnName

    def getSecondSelectedColumnName(self):
        return self.secondSelectedColumnName

    def getRelationshipType(self):
        return self.relationshipType

