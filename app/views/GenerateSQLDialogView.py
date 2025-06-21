from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QGridLayout, QHBoxLayout, QLabel, QPushButton, QWidget

from app.views.widgets.CodeEditor import CodeEditor


class GenerateSQLDialogView(QDialog):
    def __init__(self, ParentWindow):
        super().__init__(ParentWindow)

    def setupUI(self, SQLCode):
        self.setObjectName("GenerateSQLDialog")
        self.resize(600, 400)
        self.setWindowTitle("Generate SQL Code")

        self.gridLayout = QGridLayout(self)

        self.horizontalLayout = QHBoxLayout()
        self.generateSQLCodeLabel = QLabel(u"Generated SQL Code", self)
        self.generateSQLCodeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout.addWidget(self.generateSQLCodeLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.SQLCodeTextEdit = CodeEditor(self)
        self.SQLCodeTextEdit.setReadOnly(True)
        self.SQLCodeTextEdit.setPlainText(SQLCode)
        self.horizontalLayout_2.addWidget(self.SQLCodeTextEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.copyCodeButton = QPushButton(u"Copy the code", self)
        self.saveCodeButton = QPushButton(u"Save the code", self)
        self.testCodeButton = QPushButton(u"Test the code in Oracle", self)
        self.horizontalLayout_3.addWidget(self.copyCodeButton)
        self.horizontalLayout_3.addWidget(self.saveCodeButton)
        self.horizontalLayout_3.addWidget(self.testCodeButton)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_7 = QHBoxLayout()
        self.pleceholderWidget = QWidget(self)
        self.cancelButton = QPushButton(u"Cancel", self)
        self.okButton = QPushButton(u"OK", self)
        self.horizontalLayout_6.addWidget(self.pleceholderWidget)
        self.horizontalLayout_5.addWidget(self.pleceholderWidget)
        self.horizontalLayout_7.addWidget(self.cancelButton)
        self.horizontalLayout_7.addWidget(self.okButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 15)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 2)

    def displayDialog(self):
        result = self.exec()
        return result



