from app.models.ConnectionModel import ConnectionModel


class RelationshipModel(ConnectionModel):
    def __init__(self, FirstTable, SecondTable, relationshipType):
        super().__init__(FirstTable, SecondTable)
        self.relationshipType = relationshipType

    def getRelationshipType(self):
        return self.relationshipType
