from app.views.ColumnSelectionDialogView import ColumnSelectionDialogView
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
        self.RelationshipContextMenuView.setupUI()
        self.RelationshipContextMenuController = RelationshipContextMenuController(self.RelationshipContextMenuView)
        self.firstSelectedColumnName = None
        self.secondSelectedColumnName = None
        self.isFirstSelectedColumnPK = False
        self.isSecondSelectedColumnPK = False
        self.isRelationshipBeingDrawn = False
        self.isContextMenuAtWork = False

    def setFirstSelectedColumnName(self):
        obtainedTableColumns = self.FirstClickedTable.getTableColumns()

        selectedColumnName = self.displayColumnSelectionDialog(obtainedTableColumns)
        if selectedColumnName is None:
            return False
        self.firstSelectedColumnName = selectedColumnName
        return True

    def setSecondSelectedColumnName(self):
        obtainedTableColumns = self.SecondClickedTable.getTableColumns()

        selectedColumnName = self.displayColumnSelectionDialog(obtainedTableColumns)
        if selectedColumnName is None:
            return False
        self.secondSelectedColumnName = selectedColumnName
        return True

    def displayColumnSelectionDialog(self, obtainedTableColumns):
        ColumnSelectionDialog = ColumnSelectionDialogView(self.ParentWindow, obtainedTableColumns)
        return ColumnSelectionDialog.displayDialog()

    def setForeignKeys(self):
        FirstTableColumnsModel = self.FirstClickedTable.getTableColumnsModel()
        SecondTableColumnsModel = self.SecondClickedTable.getTableColumnsModel()

        if not FirstTableColumnsModel.setForeignKeyByColumnName(self.firstSelectedColumnName):
            self.isFirstSelectedColumnPK = True
        if not SecondTableColumnsModel.setForeignKeyByColumnName(self.secondSelectedColumnName):
            self.isSecondSelectedColumnPK = True

    def resetSelections(self):
        self.resetTables()
        self.firstSelectedColumnName = None
        self.secondSelectedColumnName = None
        self.isFirstSelectedColumnPK = False
        self.isSecondSelectedColumnPK = False

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
                                                         self.firstSelectedColumnName, self.secondSelectedColumnName)
        else:
            self.displayWrongRelationshipDialog()
        self.resetSelections()

    def add_1_n_Relationship(self):
        self.setForeignKeys()
        if self.isFirstSelectedColumnPK and not self.isSecondSelectedColumnPK:
            self.RelationshipsModel.add_1_n_Relationship(self.FirstClickedTable, self.SecondClickedTable,
                                                         self.firstSelectedColumnName, self.secondSelectedColumnName)
        else:
            self.displayWrongRelationshipDialog()
        self.resetSelections()

    def add_n_n_Relationship(self):
        self.setForeignKeys()
        if self.isFirstSelectedColumnPK and self.isSecondSelectedColumnPK:
            self.RelationshipsModel.add_n_n_Relationship(self.FirstClickedTable, self.SecondClickedTable,
                                                         self.firstSelectedColumnName, self.secondSelectedColumnName)
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
        self.RelationshipsModel.deleteSelectedRelationshipByTable(ObtainedTable)

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
            if self.RelationshipContextMenuController.getSelectEditRelationshipStatus():
                self.RelationshipContextMenuController.unselectEditRelationship()
                self.isContextMenuAtWork = False
                return RelationshipContextMenuEnum.EDIT
            elif self.RelationshipContextMenuController.getSelectDeleteRelationshipStatus():
                self.RelationshipContextMenuController.unselectDeleteRelationship()
                self.isContextMenuAtWork = False
                return RelationshipContextMenuEnum.DELETE
            return RelationshipContextMenuEnum.NONE

    def unselectContextMenuAtWork(self):
        self.isContextMenuAtWork = False

    def getContextMenuAtWorkStatus(self):
        return self.isContextMenuAtWork
