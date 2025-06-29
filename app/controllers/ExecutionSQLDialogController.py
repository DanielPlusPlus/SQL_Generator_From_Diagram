class ExecutionSQLDialogController:
    def __init__(self, ExecutionSQLDialogView):
        self.ExecutionSQLDialogView = ExecutionSQLDialogView

        self.ExecutionSQLDialogView.cancelButton.clicked.connect(self.selectCancel)
        self.ExecutionSQLDialogView.okButton.clicked.connect(self.selectOK)

    def selectCancel(self):
        self.ExecutionSQLDialogView.reject()

    def selectOK(self):
        self.ExecutionSQLDialogView.accept()
