import math
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint, QPointF

from app.enums.RelationshipsEnum import RelationshipsEnum


class RelationshipsView:
    def __init__(self, RelationshipsModel, ParentWindow):
        self.RelationshipsModel = RelationshipsModel
        self.ParentWindow = ParentWindow
        self.drawRelationships()

    def drawRelationships(self):
        painter = QPainter(self.ParentWindow)
        painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.PenStyle.SolidLine))
        painter.setRenderHint(QPainter.Antialiasing)

        for rel in self.RelationshipsModel.getRelationships():
            first_rect = rel.FirstTable.getRectangle()
            second_rect = rel.SecondTable.getRectangle()

            start = self.edgePoint(first_rect, second_rect)
            end = self.edgePoint(second_rect, first_rect)

            painter.drawLine(start, end)

            # Rysowanie oznaczenia relacji
            self.drawRelationshipSymbol(painter, start, end, rel.relationshipType)

        painter.end()

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

    def drawRelationshipSymbol(self, painter, start: QPoint, end: QPoint, rel_type: str):
        # Oblicz kąt linii
        angle = math.atan2(end.y() - start.y(), end.x() - start.x())

        def draw_bar(point, offset=0):
            size = 6
            perp = angle + math.pi / 2
            dx = size * math.cos(perp)
            dy = size * math.sin(perp)
            ox = offset * math.cos(angle)
            oy = offset * math.sin(angle)
            x = point.x() + ox
            y = point.y() + oy
            p1 = QPointF(x - dx, y - dy)
            p2 = QPointF(x + dx, y + dy)
            painter.drawLine(p1, p2)

        def draw_crows_foot(point):
            spread = 0.4
            length = 12
            for a in [-spread, 0, spread]:
                dx = length * math.cos(angle + a)
                dy = length * math.sin(angle + a)
                painter.drawLine(point, QPointF(point.x() + dx, point.y() + dy))

        # Rysowanie symboli w zależności od typu relacji
        if rel_type == RelationshipsEnum.REL_1_1:
            draw_bar(start, offset=12)
            draw_bar(end, offset=-12)
        elif rel_type == RelationshipsEnum.REL_1_n:
            draw_bar(start, offset=12)
            draw_crows_foot(end)
        elif rel_type == RelationshipsEnum.REL_n_n:
            draw_crows_foot(start)
            draw_crows_foot(end)
