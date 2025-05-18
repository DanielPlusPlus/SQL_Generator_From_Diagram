from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint


class RelationshipsView:
    def __init__(self, RelationshipsModel, ParentWindow):
        self.RelationshipsModel = RelationshipsModel
        self.ParentWindow = ParentWindow
        self.drawRelationships()

    def drawRelationships(self):
        Painter = QPainter(self.ParentWindow)
        Painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.PenStyle.SolidLine))

        for rel in self.RelationshipsModel.getRelationships():
            from_rect = rel.FirstTable.getRectangle()
            to_rect = rel.SecondTable.getRectangle()

            start = self.edgePoint(from_rect, to_rect.center())
            end = self.edgePoint(to_rect, from_rect.center())

            Painter.drawLine(start, end)

    def edgePoint(self, rect, target_point):
        center = rect.center()
        dx = target_point.x() - center.x()
        dy = target_point.y() - center.y()
        if dx == 0 and dy == 0:
            return center

        if abs(dx) * rect.height() > abs(dy) * rect.width():
            x = rect.right() if dx > 0 else rect.left()
            y = center.y() + dy * (x - center.x()) // dx
        else:
            y = rect.bottom() if dy > 0 else rect.top()
            x = center.x() + dx * (y - center.y()) // dy

        return QPoint(x, y)
