from app.controllers.ConnectionsController import ConnectionsController


class InheritancesController(ConnectionsController):
    def __init__(self, ParentWindow, InheritanceView, InheritanceModel, TablesModel):
        super().__init__(ParentWindow, TablesModel)
        self.InheritancesView = InheritanceView
        self.InheritancesModel = InheritanceModel
        self.isInheritanceBeingDrawn = False

    def selectInheritanceBeingDrawn(self):
        self.isInheritanceBeingDrawn = True

    def unselectInheritanceBeingDrawn(self):
        self.isInheritanceBeingDrawn = False

    def getInheritanceBeingDrawnStatus(self):
        return self.isInheritanceBeingDrawn

    def addInheritance(self):
        self.InheritancesModel.addInheritance(self.FirstClickedTable, self.SecondClickedTable)
        self.resetTables()

    def deleteInheritanceByTable(self, ObtainedTable):
        self.InheritancesModel.deleteInheritanceByTable(ObtainedTable)

    def selectDrawInheritanceBeingDrawn(self, cursorPosition):
        self.InheritancesView.drawInheritanceBeingDrawn(self.FirstClickedTable, cursorPosition)

    def selectDrawInheritances(self):
        self.InheritancesView.drawInheritances()
