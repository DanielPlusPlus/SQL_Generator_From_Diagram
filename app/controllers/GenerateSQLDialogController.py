from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QFileDialog

from app.views.InfoDialogView import InfoDialogView
from app.views.ErrorDialogView import ErrorDialogView
from app.views.ExecutionSQLDialogView import ExecutionSQLDialogView
from app.controllers.OracleDatabaseController import OracleDatabaseController
from app.controllers.ExecutionSQLDialogController import ExecutionSQLDialogController


class GenerateSQLDialogController:
    def __init__(self, ParentWindow, GenerateSQLDialogView):
        self.ParentWindow = ParentWindow
        self.GenerateSQLDialogView = GenerateSQLDialogView

        self.GenerateSQLDialogView.copyCodeButton.clicked.connect(self.selectCopyCode)
        self.GenerateSQLDialogView.saveCodeButton.clicked.connect(self.selectSaveCode)
        self.GenerateSQLDialogView.testCodeButton.clicked.connect(self.selectTestCode)
        self.GenerateSQLDialogView.cancelButton.clicked.connect(self.selectCancel)
        self.GenerateSQLDialogView.okButton.clicked.connect(self.selectOK)

    def selectCopyCode(self):
        clipboard = QGuiApplication.clipboard()
        sqlCode = self.GenerateSQLDialogView.SQLCodeTextEdit.toPlainText()

        clipboard.setText(sqlCode)

        dialogTitle = "INFORMATION"
        dialogText = "Entire SQL code has been copied to clipboard"
        InfoDialog = InfoDialogView(self.ParentWindow, dialogTitle, dialogText)
        InfoDialog.displayDialog()

    def selectSaveCode(self):
        filePath, _ = QFileDialog.getSaveFileName(
            self.GenerateSQLDialogView,
            "Save SQL Code",
            filter="SQL Files (*.sql)"
        )
        if filePath:
            try:
                sqlCode = self.GenerateSQLDialogView.SQLCodeTextEdit.toPlainText()
                with open(filePath, 'w', encoding='utf-8') as file:
                    file.write(sqlCode)
                    dialogTitle = "INFORMATION"
                    dialogText = "SQL code has been successfully saved to a file"
                    InfoDialog = InfoDialogView(self.ParentWindow, dialogTitle, dialogText)
                    InfoDialog.displayDialog()
            except Exception as e:
                dialogTitle = "ERROR"
                dialogText = f"Failed to save file:\n{str(e)}"
                ErrorDialog = ErrorDialogView(self.ParentWindow, dialogTitle, dialogText)
                ErrorDialog.displayDialog()

    def selectTestCode(self):
        sqlCode = self.GenerateSQLDialogView.SQLCodeTextEdit.toPlainText()

        if not sqlCode.strip():
            dialogTitle = "ERROR"
            dialogText = "SQL code is empty"
            ErrorDialog = ErrorDialogView(self.ParentWindow, dialogTitle, dialogText)
            ErrorDialog.displayDialog()
            return

        OracleDatabaseControl = OracleDatabaseController()
        executionResult = OracleDatabaseControl.executeSQLCode(sqlCode)

        executionSQLDialog = ExecutionSQLDialogView(self.ParentWindow)
        executionSQLDialog.setupUI(executionResult)
        executionSQLControl = ExecutionSQLDialogController(executionSQLDialog)
        executionSQLDialog.displayDialog()

    def selectCancel(self):
        self.GenerateSQLDialogView.reject()

    def selectOK(self):
        self.GenerateSQLDialogView.accept()
