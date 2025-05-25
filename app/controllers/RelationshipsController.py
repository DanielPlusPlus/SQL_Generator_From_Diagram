from app.controllers.ConnectionsController import ConnectionsController


class RelationshipsController(ConnectionsController):
    def __init__(self, RelationshipsView, RelationshipsModel, TablesModel):
        super().__init__(TablesModel)
        self.RelationshipsView = RelationshipsView
        self.RelationshipsModel = RelationshipsModel
        self.isRelationshipBeingDrawn = False

    def add_1_1_Relationship(self):
        self.RelationshipsModel.add_1_1_Relationship(self.FirstClickedTable, self.SecondClickedTable)

    def add_1_n_Relationship(self):
        self.RelationshipsModel.add_1_n_Relationship(self.FirstClickedTable, self.SecondClickedTable)

    def add_n_n_Relationship(self):
        self.RelationshipsModel.add_n_n_Relationship(self.FirstClickedTable, self.SecondClickedTable)

    def deleteRelationshipByTable(self, ObtainedTable):
        self.RelationshipsModel.deleteSelectedRelationship(ObtainedTable)

    def selectDrawRelationshipBeingDrawn(self, cursorPosition):
        self.RelationshipsView.drawRelationshipBeingDrawn(self.FirstClickedTable, cursorPosition)

    def selectDrawRelationships(self):
        self.RelationshipsView.drawRelationships()
