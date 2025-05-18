from app.enums.RelationshipsEnum import RelationshipsEnum


class RelationshipModel:
    def __init__(self, firstTable, secondTable, relationshipType):
        self.firstTable = firstTable
        self.secondTable = secondTable
        self.relationshipType = relationshipType


class RelationshipsModel:
    def __init__(self):
        self.relationships = []

    def add_1_1_Relationship(self, firstTable, secondTable):
        CreatedRelationship = RelationshipModel(firstTable, secondTable, RelationshipsEnum.REL_1_1)
        self.relationships.append(CreatedRelationship)

    def add_1_n_Relationship(self, firstTable, secondTable):
        CreatedRelationship = RelationshipModel(firstTable, secondTable, RelationshipsEnum.REL_1_n)
        self.relationships.append(CreatedRelationship)

    def add_n_n_Relationship(self, firstTable, secondTable):
        CreatedRelationship = RelationshipModel(firstTable, secondTable, RelationshipsEnum.REL_n_n)
        self.relationships.append(CreatedRelationship)
