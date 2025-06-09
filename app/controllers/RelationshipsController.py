from app.views.ConfirmationDialogView import ConfirmationDialogView
from app.views.ErrorDialogView import ErrorDialogView
from app.views.RelationshipContextMenuView import RelationshipContextMenuView
from app.controllers.ConnectionsController import ConnectionsController
from app.controllers.RelationshipContextMenuController import RelationshipContextMenuController
from app.enums.RelationshipContextMenuEnum import RelationshipContextMenuEnum


class RelationshipsController(ConnectionsController):
    def __init__(self, ParentWindow, RelationshipsView, RelationshipsModel, TablesModel):
        super().__init__(ParentWindow, TablesModel)
        self.RelationshipsView = RelationshipsView
        self.RelationshipsModel = RelationshipsModel
        self.RelationshipContextMenuView = RelationshipContextMenuView(self.ParentWindow)
        self.RelationshipContextMenuView.setup_UI()
        self.RelationContextMenuController = RelationshipContextMenuController(self.RelationshipContextMenuView)
        self.isRelationshipBeingDrawn = False
        self.isContextMenuAtWork = False

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
        if not self.isFirstSelectedColumnPK and not self.isSecondSelectedColumnPK:
            self.RelationshipsModel.add_n_n_Relationship(self.FirstClickedTable, self.SecondClickedTable,
                                                         self.FirstSelectedColumn, self.SecondSelectedColumn)
        else:
            self.displayWrongRelationshipDialog()
        self.resetSelections()

    def deleteRelationship(self, cursorPosition):
        ObtainedRelationship = self.RelationshipsModel.getRelationshipFromPosition(cursorPosition)
        if ObtainedRelationship is not None:
            dialogTitle = "WARNING"
            dialogText = "Are you sure about deleting this relationship?"
            ConfirmationDialog = ConfirmationDialogView(self.ParentWindow, dialogTitle, dialogText)
            if ConfirmationDialog.displayDialog():
                self.RelationshipsModel.deleteSelectedRelationship(ObtainedRelationship)

    def deleteRelationshipByTable(self, ObtainedTable):
        self.RelationshipsModel.deleteSelectedRelationship(ObtainedTable)

    def editRelationship(self, cursorPosition):
        print("edit")

    def selectDrawRelationshipBeingDrawn(self, cursorPosition):
        self.RelationshipsView.drawRelationshipBeingDrawn(self.FirstClickedTable, cursorPosition)

    def selectDrawRelationships(self):
        self.RelationshipsView.drawRelationships()

    def displayWrongRelationshipDialog(self):
        dialogTitle = "ERROR"
        dialogText = "You choose the wrong type of relationship"
        WrongRelationshipDialog = ErrorDialogView(self.ParentWindow, dialogTitle, dialogText)
        WrongRelationshipDialog.displayDialog()

    def displayRelationshipContextMenu(self, cursorPosition, globalCursorPosition):
        ObtainedRelationship = self.RelationshipsModel.getRelationshipFromPosition(cursorPosition)
        if ObtainedRelationship is not None:
            self.isContextMenuAtWork = True
            self.RelationshipContextMenuView.exec(globalCursorPosition)
            if self.RelationContextMenuController.getSelectEditRelationshipStatus():
                self.RelationContextMenuController.unselectEditRelationship()
                self.isContextMenuAtWork = False
                return RelationshipContextMenuEnum.EDIT
            elif self.RelationContextMenuController.getSelectDeleteRelationshipStatus():
                self.RelationContextMenuController.unselectDeleteRelationship()
                self.isContextMenuAtWork = False
                return RelationshipContextMenuEnum.DELETE
            return RelationshipContextMenuEnum.NONE

    def unselectContextMenuAtWork(self):
        self.isContextMenuAtWork = False

    def getContextMenuAtWorkStatus(self):
        return self.isContextMenuAtWork
