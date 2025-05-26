from app.models.RelationshipModel import RelationshipModel
from app.enums.RelationshipsEnum import RelationshipsEnum


class RelationshipsModel:
    def __init__(self):
        self.relationships = []

    def add_1_1_Relationship(self, FirstTable, SecondTable):
        CreatedRelationship = RelationshipModel(FirstTable, SecondTable, RelationshipsEnum.REL_1_1)
        self.relationships.append(CreatedRelationship)

    def add_1_n_Relationship(self, FirstTable, SecondTable):
        CreatedRelationship = RelationshipModel(FirstTable, SecondTable, RelationshipsEnum.REL_1_n)
        self.relationships.append(CreatedRelationship)

    def add_n_n_Relationship(self, FirstTable, SecondTable):
        CreatedRelationship = RelationshipModel(FirstTable, SecondTable, RelationshipsEnum.REL_n_n)
        self.relationships.append(CreatedRelationship)

    def clearRelationships(self):
        self.relationships.clear()

    def getRelationships(self):
        return self.relationships

    def deleteSelectedRelationship(self, SelectedRelationship):
        self.relationships.remove(SelectedRelationship)

    def deleteRelationshipByTable(self, ObtainedTable):
        self.relationships = [
            relationship for relationship in self.relationships
            if relationship.getFirstTable() is not ObtainedTable and relationship.getSecondTable() is not ObtainedTable
        ]
