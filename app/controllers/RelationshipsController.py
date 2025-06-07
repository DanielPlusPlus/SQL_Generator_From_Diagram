from app.views.ErrorDialogView import ErrorDialogView
from app.controllers.ConnectionsController import ConnectionsController


class RelationshipsController(ConnectionsController):
    def __init__(self, ParentWindow, RelationshipsView, RelationshipsModel, TablesModel):
        super().__init__(ParentWindow, TablesModel)
        self.RelationshipsView = RelationshipsView
        self.RelationshipsModel = RelationshipsModel
        self.isRelationshipBeingDrawn = False

    def selectRelationshipBeingDrawn(self):
        self.isRelationshipBeingDrawn = True

    def unselectRelationshipBeingDrawn(self):
        self.isRelationshipBeingDrawn = False

    def getRelationshipBeingDrawnStatus(self):
        return self.isRelationshipBeingDrawn

    def add_1_1_Relationship(self):
        self.setForeignKeys()
        if self.isFirstSelectedColumnPK and self.isSecondSelectedColumnPK:
            self.RelationshipsModel.add_1_1_Relationship(self.FirstClickedTable, self.SecondClickedTable,
                                                         self.FirstSelectedColumn, self.SecondSelectedColumn)
        else:
            self.displayWrongRelationshipDialog()
        self.resetSelections()

    def add_1_n_Relationship(self):
        self.setForeignKeys()
        if self.isFirstSelectedColumnPK and not self.isSecondSelectedColumnPK:
            self.RelationshipsModel.add_1_n_Relationship(self.FirstClickedTable, self.SecondClickedTable,
                                                         self.FirstSelectedColumn, self.SecondSelectedColumn)
        else:
            self.displayWrongRelationshipDialog()
        self.resetSelections()

    def add_n_n_Relationship(self):
        self.setForeignKeys()
        if not self.isFirstSelectedColumnPK and self.isSecondSelectedColumnPK:
            self.RelationshipsModel.add_n_n_Relationship(self.FirstClickedTable, self.SecondClickedTable,
                                                         self.FirstSelectedColumn, self.SecondSelectedColumn)
        else:
            self.displayWrongRelationshipDialog()
        self.resetSelections()

    def deleteRelationshipByTable(self, ObtainedTable):
        self.RelationshipsModel.deleteSelectedRelationship(ObtainedTable)

    def selectDrawRelationshipBeingDrawn(self, cursorPosition):
        self.RelationshipsView.drawRelationshipBeingDrawn(self.FirstClickedTable, cursorPosition)

    def selectDrawRelationships(self):
        self.RelationshipsView.drawRelationships()

    def displayWrongRelationshipDialog(self):
        dialogTitle = "ERROR"
        dialogText = "You choose the wrong type of relationship"
        WrongRelationshipDialog = ErrorDialogView(self.ParentWindow, dialogTitle, dialogText)
        WrongRelationshipDialog.displayDialog()
