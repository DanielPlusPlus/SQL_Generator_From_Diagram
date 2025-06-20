from PySide6.QtCore import Qt, QRect, QSize
from PySide6.QtGui import QColor, QPainter, QTextFormat, QFont
from PySide6.QtWidgets import (QDialog, QGridLayout, QHBoxLayout, QLabel, QPushButton, QWidget,
                               QPlainTextEdit, QTextEdit)


class GenerateSQLDialogView(QDialog):
    def __init__(self, ParentWindow):
        super().__init__(ParentWindow)

    def setupUI(self, SQLCode):
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
        self.SQLCodeTextEdit = CodeEditor(self)
        self.SQLCodeTextEdit.setReadOnly(True)
        self.SQLCodeTextEdit.setPlainText(SQLCode)
        self.horizontalLayout_2.addWidget(self.SQLCodeTextEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

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
        self.gridLayout.setRowStretch(1, 15)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 2)

    def displayDialog(self):
        result = self.exec()
        return result


class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.code_editor = editor

    def sizeHint(self):
        return QSize(self.code_editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        self.code_editor.line_number_area_paint_event(event)


class CodeEditor(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        font = QFont("Courier", 10)
        self.setFont(font)

        self.line_number_area = LineNumberArea(self)

        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)

        self.update_line_number_area_width(0)
        self.highlight_current_line()

    def line_number_area_width(self):
        digits = len(str(max(1, self.blockCount())))
        return 10 + self.fontMetrics().horizontalAdvance('9') * digits

    def update_line_number_area_width(self, _):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.line_number_area.setGeometry(QRect(cr.left(), cr.top(), self.line_number_area_width(), cr.height()))

    def line_number_area_paint_event(self, event):
        painter = QPainter(self.line_number_area)
        painter.fillRect(event.rect(), QColor(240, 240, 240))

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = int(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + int(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(Qt.gray)
                painter.drawText(0, top, self.line_number_area.width() - 5, self.fontMetrics().height(),
                                 Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + int(self.blockBoundingRect(block).height())
            block_number += 1

    def highlight_current_line(self):
        extra_selections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            line_color = QColor(232, 242, 254)
            selection.format.setBackground(line_color)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extra_selections.append(selection)
        self.setExtraSelections(extra_selections)
