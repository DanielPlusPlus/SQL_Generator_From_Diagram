from app.views.ColumnSelectionDialogView import ColumnSelectionDialogView


class ConnectionsController:
    def __init__(self, ParentWindow, TablesModel):
        self.ParentWindow = ParentWindow
        self.TablesModel = TablesModel
        self.FirstClickedTable = None
        self.SecondClickedTable = None
        self.firstSelectedColumnName = None
        self.secondSelectedColumnName = None
        self.isFirstSelectedColumnPK = False
        self.isSecondSelectedColumnPK = False

    def setFirstClickedTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)

        if ObtainedTable is not None:
            self.FirstClickedTable = ObtainedTable
            ObtainedTableColumns = ObtainedTable.getTableColumns()

            ColumnSelectionDialog = ColumnSelectionDialogView(self.ParentWindow, ObtainedTableColumns)
            selectedColumnName = ColumnSelectionDialog.displayDialog()

            if selectedColumnName is None:
                return False
            self.firstSelectedColumnName = selectedColumnName

            return True
        return False

    def setSecondClickedTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)

        if ObtainedTable is not None:
            self.SecondClickedTable = ObtainedTable
            ObtainedTableColumns = ObtainedTable.getTableColumns()

            ColumnSelectionDialog = ColumnSelectionDialogView(self.ParentWindow, ObtainedTableColumns)
            selectedColumnName = ColumnSelectionDialog.displayDialog()

            if selectedColumnName is None:
                return False
            self.secondSelectedColumnName = selectedColumnName

            return True
        return False

    def setForeignKeys(self):
        FirstTableColumnsModel = self.FirstClickedTable.getTableColumnsModel()
        SecondTableColumnsModel = self.SecondClickedTable.getTableColumnsModel()

        if not FirstTableColumnsModel.setForeignKeyByColumnName(self.firstSelectedColumnName):
            self.isFirstSelectedColumnPK = True
        if not SecondTableColumnsModel.setForeignKeyByColumnName(self.secondSelectedColumnName):
            self.isSecondSelectedColumnPK = True

    def resetSelections(self):
        self.FirstClickedTable = None
        self.SecondClickedTable = None
        self.firstSelectedColumnName = None
        self.secondSelectedColumnName = None
        self.isFirstSelectedColumnPK = False
        self.isSecondSelectedColumnPK = False
