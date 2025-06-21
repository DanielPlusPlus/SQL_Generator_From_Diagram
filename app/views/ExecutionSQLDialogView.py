from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialog, QGridLayout, QHBoxLayout, QLabel, QPushButton, QWidget, QTextEdit


class ExecutionSQLDialogView(QDialog):
    def __init__(self, ParentWindow):
        super().__init__(ParentWindow)

    def setupUI(self, executionResult):
        self.setObjectName("ExecuteSQLDialog")
        self.resize(600, 400)
        self.setWindowTitle("Execute SQL Code")

        self.gridLayout = QGridLayout(self)

        self.horizontalLayout = QHBoxLayout()
        self.executeSQLCodeLabel = QLabel(u"Execution SQL Code Result", self)
        self.executeSQLCodeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout.addWidget(self.executeSQLCodeLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.ExecutionResultTextEdit = QTextEdit(self)
        font = QFont("Courier", 10)
        self.ExecutionResultTextEdit.setFont(font)
        self.ExecutionResultTextEdit.setReadOnly(True)
        self.ExecutionResultTextEdit.setPlainText(executionResult)
        self.horizontalLayout_2.addWidget(self.ExecutionResultTextEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_6 = QHBoxLayout()
        self.pleceholderWidget = QWidget(self)
        self.cancelButton = QPushButton(u"Cancel", self)
        self.okButton = QPushButton(u"OK", self)
        self.horizontalLayout_5.addWidget(self.pleceholderWidget)
        self.horizontalLayout_4.addWidget(self.pleceholderWidget)
        self.horizontalLayout_6.addWidget(self.cancelButton)
        self.horizontalLayout_6.addWidget(self.okButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 17)
        self.gridLayout.setRowStretch(2, 2)

    def displayDialog(self):
        result = self.exec()
        return result
