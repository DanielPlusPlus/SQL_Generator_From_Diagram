from app.models.ConnectionModel import ConnectionModel


class RelationshipModel(ConnectionModel):
    def __init__(self, FirstTable, SecondTable, FirstSelectedColumn, SecondSelectedColumn, relationshipType):
        super().__init__(FirstTable, SecondTable, FirstSelectedColumn, SecondSelectedColumn)
        self.relationshipType = relationshipType

    def getRelationshipType(self):
        return self.relationshipType
