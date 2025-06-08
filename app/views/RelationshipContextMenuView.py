from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction


class RelationshipContextMenuView(QMenu):
    def __init__(self, ParentWindow):
        super().__init__(ParentWindow)

    def setup_UI(self):
        self.actionEditRelationship = QAction("Edit relationship", self)
        self.actionDeleteRelationship = QAction("Delete relationship", self)

        self.addAction(self.actionEditRelationship)
        self.addAction(self.actionDeleteRelationship)