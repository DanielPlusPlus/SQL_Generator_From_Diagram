from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QPushButton, QLabel, QWidget
)
from PySide6.QtGui import QFont, QTextOption
from PySide6.QtCore import Qt


class GenerateSQLDialogView(QDialog):
    def __init__(self, parent=None, generated_code=""):
        super().__init__(parent)
        self.generated_code = generated_code

    def setupUI(self):
        self.setWindowTitle("Generated SQL Code")
        self.resize(600, 400)
        main_layout = QVBoxLayout(self)

        label = QLabel("Generated SQL Code:")
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(label)

        self.code_editor = QPlainTextEdit(self)
        self.code_editor.setPlainText(self.generated_code)
        self.code_editor.setReadOnly(True)
        self.code_editor.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.code_editor.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        self.code_editor.setFont(QFont("Courier", 10))
        main_layout.addWidget(self.code_editor, stretch=1)

        button_layout = QHBoxLayout()
        self.copy_button = QPushButton("COPY", self)
        self.test_sql_button = QPushButton("TEST SQL", self)
        button_layout.addStretch()
        button_layout.addWidget(self.copy_button)
        button_layout.addWidget(self.test_sql_button)

        main_layout.addLayout(button_layout)

    def set_code(self, code: str):
        self.generated_code = code
        self.code_editor.setPlainText(code)

    def get_code(self) -> str:
        return self.code_editor.toPlainText()

    def displayDialog(self):
        result = self.exec()
        return result
