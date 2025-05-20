class RelationshipsController:
    def __init__(self, RelationshipsView, RelationshipsModel, TablesModel):
        self.RelationshipsView = RelationshipsView
        self.RelationshipsModel = RelationshipsModel
        self.TablesModel = TablesModel
        self.FirstClickedTable = None
        self.SecondClickedTable = None
        self.isRelationshipBeingDrawn = None

    def setFirstClickedTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            self.FirstClickedTable = ObtainedTable
            return True
        return False

    def setSecondClickedTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            self.SecondClickedTable = ObtainedTable
            return True
        return False

    def selectRelationshipBeingDrawn(self):
        self.isRelationshipBeingDrawn = True

    def unselectRelationshipBeingDrawn(self):
        self.isRelationshipBeingDrawn = False

    def getRelationshipBeingDrawnStatus(self):
        return self.isRelationshipBeingDrawn

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

