from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog, QGridLayout, QHBoxLayout,
                               QLabel, QPushButton, QTextEdit,
                               QWidget)


class GenerateSQLDialogView(QDialog):
    def __init__(self, ParentWindow):
        super().__init__(ParentWindow)

    def setupUI(self):
        self.setObjectName("GenerateSQLDialog")
        self.resize(600, 400)
        self.setWindowTitle("Generate SQL Code")

        self.gridLayout = QGridLayout(self)

        self.horizontalLayout = QHBoxLayout()
        self.generateSQLLabel = QLabel(u"Generated SQL Code", self)
        self.generateSQLLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout.addWidget(self.generateSQLLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.SQLCodeTextEdit = QTextEdit(self)
        self.horizontalLayout_2.addWidget(self.SQLCodeTextEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.pushButton_1 = QPushButton(u"Copy the code", self)
        self.horizontalLayout_3.addWidget(self.pushButton_1)
        self.pushButton_2 = QPushButton(u"Test the code in Oracle", self)
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_7 = QHBoxLayout()
        self.pleceholderWidget = QWidget(self)
        self.pushButton_3 = QPushButton(u"Cancel", self)
        self.pushButton_4 = QPushButton(u"OK", self)
        self.horizontalLayout_6.addWidget(self.pleceholderWidget)
        self.horizontalLayout_5.addWidget(self.pleceholderWidget)
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)

    def displayDialog(self):
        result = self.exec()
        return result

