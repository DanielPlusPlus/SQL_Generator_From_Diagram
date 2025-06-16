from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import QPoint


class ExportDiagramController:
    def __init__(self, ScrollAreaView):
        self.ScrollAreaView = ScrollAreaView

    def exportDiagramToPNG(self):
        widget = self.ScrollAreaView.widget()
        if widget is None:
            print("No export widget")
            return

        pixmap = QPixmap(widget.size())
        pixmap.fill()

        painter = QPainter(pixmap)
        widget.render(painter, QPoint(0, 0))
        painter.end()

        filePath, _ = QFileDialog.getSaveFileName(
            None,
            "Save diagram as PNG",
            "",
            "PNG files (*.png)"
        )
        if not filePath:
            print("Save canceled")
            return

        pixmap.save(filePath, "PNG")
        print(f"Diagram saved to: {filePath}")
