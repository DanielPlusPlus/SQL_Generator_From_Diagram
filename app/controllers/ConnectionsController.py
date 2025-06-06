from app.views.ColumnSelectionDialogView import ColumnSelectionDialogView


class ConnectionsController:
    def __init__(self, ParentWindow, TablesModel):
        self.ParentWindow = ParentWindow
        self.TablesModel = TablesModel
        self.FirstClickedTable = None
        self.SecondClickedTable = None

    def setFirstClickedTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            self.FirstClickedTable = ObtainedTable
            ObtainedTableColumns = ObtainedTable.getTableColumns()
            ColumnSelectionDialog = ColumnSelectionDialogView(self.ParentWindow, ObtainedTableColumns)
            result = ColumnSelectionDialog.displayDialog()
            if result is None:
                return False
            return True
        return False

    def setSecondClickedTable(self, cursorPosition):
        ObtainedTable = self.TablesModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            self.SecondClickedTable = ObtainedTable
            ObtainedTableColumns = ObtainedTable.getTableColumns()
            ColumnSelectionDialog = ColumnSelectionDialogView(self.ParentWindow, ObtainedTableColumns)
            result = ColumnSelectionDialog.displayDialog()
            if result is None:
                return False
            return True
        return False
