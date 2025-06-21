from app.views.ConfirmationDialogView import ConfirmationDialogView
from app.views.InheritanceContextMenuView import InheritanceContextMenuView
from app.controllers.ConnectionsController import ConnectionsController
from app.controllers.InheritanceContextMenuController import InheritanceContextMenuController
from app.enums.InheritanceContextMenuEnum import InheritanceContextMenuEnum


class InheritancesController(ConnectionsController):
    def __init__(self, ParentWindow, InheritanceView, InheritanceModel, TablesModel):
        super().__init__(ParentWindow, TablesModel)
        self.InheritancesView = InheritanceView
        self.InheritancesModel = InheritanceModel
        self.InheritanceContextMenuView = InheritanceContextMenuView(self.ParentWindow)
        self.InheritanceContextMenuView.setupUI()
        self.InheritanceContextMenuController = InheritanceContextMenuController(self.InheritanceContextMenuView)
        self.isInheritanceBeingDrawn = False
        self.isContextMenuAtWork = False

    def selectInheritanceBeingDrawn(self):
        self.isInheritanceBeingDrawn = True

    def unselectInheritanceBeingDrawn(self):
        self.isInheritanceBeingDrawn = False

    def getInheritanceBeingDrawnStatus(self):
        return self.isInheritanceBeingDrawn

    def addInheritance(self):
        self.InheritancesModel.addInheritance(self.FirstClickedTable, self.SecondClickedTable)
        self.resetTables()

    def deleteInheritance(self, cursorPosition):
        ObtainedInheritance = self.InheritancesModel.getInheritanceFromPosition(cursorPosition)
        if ObtainedInheritance is not None:
            dialogTitle = "WARNING"
            dialogText = "Are you sure about deleting this inheritance?"
            ConfirmationDialog = ConfirmationDialogView(self.ParentWindow, dialogTitle, dialogText)
            if ConfirmationDialog.displayDialog():
                self.InheritancesModel.deleteSelectedInheritance(ObtainedInheritance)

    def deleteInheritanceByTable(self, ObtainedTable):
        self.InheritancesModel.deleteInheritanceByTable(ObtainedTable)

    def editInheritance(self, cursorPosition):
        print("edit")

    def selectDrawInheritanceBeingDrawn(self, cursorPosition):
        self.InheritancesView.drawInheritanceBeingDrawn(self.FirstClickedTable, cursorPosition)

    def selectDrawInheritances(self):
        self.InheritancesView.drawInheritances()

    def displayInheritanceContextMenu(self, cursorPosition, globalCursorPosition):
        ObtainedRelationship = self.InheritancesModel.getInheritanceFromPosition(cursorPosition)
        if ObtainedRelationship is not None:
            self.isContextMenuAtWork = True
            self.InheritanceContextMenuView.exec(globalCursorPosition)
            if self.InheritanceContextMenuController.getSelectEditInheritanceStatus():
                self.InheritanceContextMenuController.unselectEditInheritance()
                self.isContextMenuAtWork = False
                return InheritanceContextMenuEnum.EDIT
            elif self.InheritanceContextMenuController.getSelectDeleteInheritanceStatus():
                self.InheritanceContextMenuController.unselectDeleteInheritance()
                self.isContextMenuAtWork = False
                return InheritanceContextMenuEnum.DELETE
            return InheritanceContextMenuEnum.NONE

    def unselectContextMenuAtWork(self):
        self.isContextMenuAtWork = False

    def getContextMenuAtWorkStatus(self):
        return self.isContextMenuAtWork
