from app.views.ConfirmationDialogView import ConfirmationDialogView
from app.views.TableContextMenuView import TableContextMenuView
from app.views.EditTableDialogView import EditTableDialogView
from app.controllers.TableContextMenuController import TableContextMenuController
from app.controllers.EditTableDialogController import EditTableDialogController
from app.enums.TableContextMenuEnum import TableContextMenuEnum


class TablesController:
    def __init__(self, ParentWindow, TablesView, TablesModel, RelationshipsController, InheritancesController):
        self.ParentWindow = ParentWindow
        self.TablesView = TablesView
        self.TablesModel = TablesModel
        self.RelationshipsController = RelationshipsController
        self.InheritancesController = InheritancesController
        self.TableContextMenuView = TableContextMenuView(self.ParentWindow)
        self.TableContextMenuView.setup_UI()
        self.TableContextMenuController = TableContextMenuController(self.TableContextMenuView)
        self.TableInTransfer = None
        self.isTableInTransfer = False
        self.isContextMenuAtWork = False

    def addTable(self, cursorPosition):
        self.TablesModel.addTable(cursorPosition)

    def deleteTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            dialogTitle = "WARNING"
            dialogText = "Are you sure about deleting this table?"
            ConfirmationDialog = ConfirmationDialogView(self.ParentWindow, dialogTitle, dialogText)
            if ConfirmationDialog.displayDialog():
                self.TablesModel.deleteSelectedTable(ObtainedTable)
                self.RelationshipsController.deleteRelationshipByTable(ObtainedTable)
                self.InheritancesController.deleteInheritanceByTable(ObtainedTable)

    def editTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            EditTableDialog = EditTableDialogView(self.ParentWindow, ObtainedTable)
            EditTableDialog.setupUi()
            EditTableDialogControl = EditTableDialogController(EditTableDialog, ObtainedTable)
            EditTableDialog.displayDialog()

    def selectTableInTransfer(self, cursorPosition):
        self.TableInTransfer = self.TablesModel.getTableFromPosition(cursorPosition)
        if self.TableInTransfer is not None:
            self.isTableInTransfer = True

    def unselectTableInTransfer(self, cursorPosition):
        self.TableInTransfer.changeTablePosition(cursorPosition.x(), cursorPosition.y())
        self.isTableInTransfer = False
        self.TableInTransfer = None

    def updateTableInTransferPosition(self, cursorPosition):
        self.TableInTransfer.changeTablePosition(cursorPosition.x(), cursorPosition.y())

    def selectDrawTempTable(self, cursorPosition):
        self.TablesView.drawTempTable(cursorPosition)

    def selectDrawTables(self):
        self.TablesView.drawTables()

    def getTableInTransferStatus(self):
        return self.isTableInTransfer

    def displayTableContextMenu(self, cursorPosition, globalCursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            self.isContextMenuAtWork = True
            self.TableContextMenuView.exec(globalCursorPosition)
            if self.TableContextMenuController.getSelectEditTableStatus():
                self.TableContextMenuController.unselectEditTable()
                self.isContextMenuAtWork = False
                return TableContextMenuEnum.EDIT
            elif self.TableContextMenuController.getSelectDeleteTableStatus():
                self.TableContextMenuController.unselectDeleteTable()
                self.isContextMenuAtWork = False
                return TableContextMenuEnum.DELETE
            return TableContextMenuEnum.NONE

    def unselectContextMenuAtWork(self):
        self.isContextMenuAtWork = False

    def getContextMenuAtWorkStatus(self):
        return self.isContextMenuAtWork
