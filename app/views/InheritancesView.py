import math
from PySide6.QtGui import QPainter, QPen, QColor, QPolygonF
from PySide6.QtCore import Qt, QPoint, QPointF


class InheritancesView:
    def __init__(self, InheritanceModel, ParentWindow):
        self.InheritanceModel = InheritanceModel
        self.ParentWindow = ParentWindow
        self.drawInheritances()

    def drawInheritances(self):
        painter = QPainter(self.ParentWindow)
        painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.SolidLine))
        painter.setRenderHint(QPainter.Antialiasing)

        for inheritance in self.InheritanceModel.getInheritances():
            child_rect = inheritance.FirstTable.getRectangle()
            parent_rect = inheritance.SecondTable.getRectangle()

            start = self.edgePoint(child_rect, parent_rect)
            arrow_tip = self.edgePoint(parent_rect, child_rect)

            # Oblicz punkt, w którym kończy się linia (przed strzałką)
            cutoff_distance = 16  # długość odcięcia linii przed strzałką
            angle = math.atan2(arrow_tip.y() - start.y(), arrow_tip.x() - start.x())
            line_end = QPointF(
                arrow_tip.x() - cutoff_distance * math.cos(angle),
                arrow_tip.y() - cutoff_distance * math.sin(angle)
            )

            # Rysowanie linii dziedziczenia
            painter.drawLine(start, line_end)

            # Rysowanie pustej strzałki dziedziczenia
            self.drawInheritanceArrow(painter, arrow_tip, angle)

        painter.end()

    def drawInheritanceArrow(self, painter, tip: QPoint, angle: float):
        arrow_length = 16
        arrow_width = 10

        left_angle = angle + math.radians(30)
        right_angle = angle - math.radians(30)

        left = QPointF(
            tip.x() - arrow_length * math.cos(left_angle),
            tip.y() - arrow_length * math.sin(left_angle)
        )
        right = QPointF(
            tip.x() - arrow_length * math.cos(right_angle),
            tip.y() - arrow_length * math.sin(right_angle)
        )

        triangle = QPolygonF([left, tip, right])

        # Rysujemy tylko kontur trójkąta (pusta strzałka)
        painter.setBrush(Qt.NoBrush)
        painter.drawPolygon(triangle)

    def edgePoint(self, start_rect, end_rect):
        center_start = start_rect.center()
        center_end = end_rect.center()

        dx = center_end.x() - center_start.x()
        dy = center_end.y() - center_start.y()

        if dx == 0 and dy == 0:
            return center_start

        if abs(dx) * start_rect.height() > abs(dy) * start_rect.width():
            x = start_rect.right() if dx > 0 else start_rect.left()
            y = center_start.y() + dy * (x - center_start.x()) // dx
        else:
            y = start_rect.bottom() if dy > 0 else start_rect.top()
            x = center_start.x() + dx * (y - center_start.y()) // dy

        return QPoint(x, y)

    def drawInheritanceBeingDrawn(self, FirstTable, cursorPosition):
        painter = QPainter(self.ParentWindow)
        painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.DashLine))
        painter.setRenderHint(QPainter.Antialiasing)

        first_rect = FirstTable.getRectangle()
        start = self.edgePointToPoint(first_rect, cursorPosition)

        end = cursorPosition if isinstance(cursorPosition, QPoint) else QPoint(cursorPosition.x(), cursorPosition.y())
        painter.drawLine(start, end)
        painter.end()

    def edgePointToPoint(self, start_rect, end_pos):
        center_start = start_rect.center()

        if isinstance(end_pos, QPoint):
            center_end = end_pos
        else:
            center_end = end_pos.center()

        dx = center_end.x() - center_start.x()
        dy = center_end.y() - center_start.y()

        if dx == 0 and dy == 0:
            return center_start

        if abs(dx) * start_rect.height() > abs(dy) * start_rect.width():
            x = start_rect.right() if dx > 0 else start_rect.left()
            y = center_start.y() + dy * (x - center_start.x()) // dx
        else:
            y = start_rect.bottom() if dy > 0 else start_rect.top()
            x = center_start.x() + dx * (y - center_start.y()) // dy

        return QPoint(x, y)
