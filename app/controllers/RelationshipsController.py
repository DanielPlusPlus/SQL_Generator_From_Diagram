class RelationshipsController:
    def __init__(self, RelationshipsView, RelationshipsModel, TablesModel):
        self.RelationshipsView = RelationshipsView
        self.RelationshipsModel = RelationshipsModel
        self.TablesModel = TablesModel
        self.FirstClickedTable = None
        self.SecondClickedTable = None

    def setFirstClickedTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            self.FirstClickedTable = ObtainedTable

    def setSecondClickedTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            self.SecondClickedTable = ObtainedTable

    def add_1_1_Relationship(self):
        self.RelationshipsModel.add_1_1_Relationship(self.FirstClickedTable, self.SecondClickedTable)

    def add_1_n_Relationship(self):
        pass

    def add_n_n_Relationship(self):
        pass

    def selectDrawRelationships(self):
        self.RelationshipsView.drawRelationships()
