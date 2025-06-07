from app.views.ColumnSelectionDialogView import ColumnSelectionDialogView


class ConnectionsController:
    def __init__(self, ParentWindow, TablesModel):
        self.ParentWindow = ParentWindow
        self.TablesModel = TablesModel
        self.FirstClickedTable = None
        self.SecondClickedTable = None
        self.FirstSelectedColumn = None
        self.SecondSelectedColumn = None

    def setFirstClickedTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)

        if ObtainedTable is not None:
            self.FirstClickedTable = ObtainedTable
            ObtainedTableColumns = ObtainedTable.getTableColumns()

            ColumnSelectionDialog = ColumnSelectionDialogView(self.ParentWindow, ObtainedTableColumns)
            SelectedColumn = ColumnSelectionDialog.displayDialog()

            if SelectedColumn is None:
                return False
            self.FirstSelectedColumn = SelectedColumn

            return True
        return False

    def setSecondClickedTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)

        if ObtainedTable is not None:
            self.SecondClickedTable = ObtainedTable
            ObtainedTableColumns = ObtainedTable.getTableColumns()

            ColumnSelectionDialog = ColumnSelectionDialogView(self.ParentWindow, ObtainedTableColumns)
            SelectedColumn = ColumnSelectionDialog.displayDialog()

            if SelectedColumn is None:
                return False
            self.SecondSelectedColumn = SelectedColumn

            self.setForeignKeys()

            return True
        return False

    def setForeignKeys(self):
        FirstTableColumnsModel = self.FirstClickedTable.getTableColumnsModel()
        SecondTableColumnsModel = self.SecondClickedTable.getTableColumnsModel()

        FirstTableColumnsModel.setForeignKey(self.FirstSelectedColumn)
        SecondTableColumnsModel.setForeignKey(self.SecondSelectedColumn)

    def resetSelections(self):
        self.FirstClickedTable = None
        self.SecondClickedTable = None
        self.FirstSelectedColumn = None
        self.SecondSelectedColumn = None
