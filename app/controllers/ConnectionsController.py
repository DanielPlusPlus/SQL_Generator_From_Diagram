class ConnectionsController:
    def __init__(self, ParentWindow, TablesModel):
        self._ParentWindow = ParentWindow
        self.__TablesModel = TablesModel
        self.FirstClickedTable = None
        self.SecondClickedTable = None

    def setFirstClickedTable(self, cursorPosition):
        ObtainedTable = self.__TablesModel.getTableFromPosition(cursorPosition)

        if ObtainedTable is not None:
            self.FirstClickedTable = ObtainedTable
            return True
        return False

    def setSecondClickedTable(self, cursorPosition):
        ObtainedTable = self.__TablesModel.getTableFromPosition(cursorPosition)

        if ObtainedTable is not None:
            self.SecondClickedTable = ObtainedTable
            return True
        return False

    def resetTables(self):
        self.FirstClickedTable = None
        self.SecondClickedTable = None
