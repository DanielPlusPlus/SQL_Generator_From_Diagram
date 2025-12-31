from app.models.TableColumnsModel import TableColumnsModel

from copy import deepcopy


class EditTableDialogController:
    def __init__(self, EditTableDialogView, ObtainedTable):
        self.__EditTableDialogView = EditTableDialogView
        self.__ObtainedTable = ObtainedTable

        ObtainedTableColumnsModel = ObtainedTable.getTableColumnsModel()
        originalColumns = ObtainedTableColumnsModel.getColumns()
        copiedColumns = deepcopy(originalColumns)

        self.__TempTableColumnsModel = TableColumnsModel(copiedColumns)
        self.__isEditColumnSelected = False
        self.__EditTableDialogView.tableView.setModel(self.__TempTableColumnsModel)

        self.__EditTableDialogView.addColumnButton.clicked.connect(self.__selectAddColumn)
        self.__EditTableDialogView.deleteColumnButton.clicked.connect(self.__selectDeleteColumn)
        self.__EditTableDialogView.editColumnButton.clicked.connect(self.__selectEditColumn)
        self.__EditTableDialogView.cancelButton.clicked.connect(self.__selectCancel)
        self.__EditTableDialogView.okButton.clicked.connect(self.__selectOK)

    def __selectAddColumn(self):
        columnName = self.__EditTableDialogView.columnNameLineEdit.text()
        dataType = self.__EditTableDialogView.dataTypeComboBox.currentText()
        length = self.__EditTableDialogView.lengthSpinBox.value()

        self.__TempTableColumnsModel.addColumn(dataType, length, columnName)

        self.__EditTableDialogView.columnNameLineEdit.clear()
        self.__EditTableDialogView.dataTypeComboBox.setCurrentIndex(0)
        self.__EditTableDialogView.lengthSpinBox.setValue(0)

    def __selectDeleteColumn(self):
        selectedRows = self.__EditTableDialogView.tableView.selectionModel().selectedRows()
        if selectedRows:
            selectedRowNumber = selectedRows[0].row()
            self.__TempTableColumnsModel.deleteColumn(selectedRowNumber)

    def __selectEditColumn(self):  # deprecated
        self.__isEditColumnSelected = True

    def __unselectEditColumn(self):  # deprecated
        self.__isEditColumnSelected = False

    def __getSelectEditColumnStatus(self):  # deprecated
        return self.__isEditColumnSelected

    def __selectCancel(self):
        self.__EditTableDialogView.reject()

    def __selectOK(self):
        self.__editTableName()
        self.__editTableColumns()
        self.__editTableDimensions()
        self.__EditTableDialogView.accept()

    def __editTableName(self):
        newName = self.__EditTableDialogView.tableNameLineEdit.text()
        self.__ObtainedTable.editTableName(newName)

    def __editTableColumns(self):
        self.__ObtainedTable.changeTableColumnsModel(self.__TempTableColumnsModel)

    def __editTableDimensions(self):
        self.__ObtainedTable.changeTableDimensions()
