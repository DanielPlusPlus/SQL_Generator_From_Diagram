from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox


# do poprawy

class ColumnSelectionDialogView(QDialog):
    def __init__(self, ParentWindow, ObtainedTableColumns):
        super().__init__(ParentWindow)
        self.setWindowTitle("Select Column")
        self.selected_column = None

        layout = QVBoxLayout(self)

        label = QLabel("Wybierz kolumnę:")
        layout.addWidget(label)

        self.combo_box = QComboBox()
        self.combo_box.addItems([col["columnName"] for col in ObtainedTableColumns])
        layout.addWidget(self.combo_box)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def displayDialog(self):
        if self.exec() == QDialog.Accepted:
            return self.combo_box.currentText() or None
        return None
