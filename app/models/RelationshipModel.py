from app.models.ConnectionModel import ConnectionModel


class RelationshipModel(ConnectionModel):
    def __init__(self, FirstTable, SecondTable, firstSelectedColumnName, secondSelectedColumnName, relationshipType):
        super().__init__(FirstTable, SecondTable, firstSelectedColumnName, secondSelectedColumnName)
        self.relationshipType = relationshipType

    def getRelationshipType(self):
        return self.relationshipType

