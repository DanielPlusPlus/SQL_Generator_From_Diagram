class RelationshipContextMenuController:
    def __init__(self, RelationshipContextMenuView):
        self.isEditRelationshipSelected = False
        self.isDeleteRelationshipSelected = False
        RelationshipContextMenuView.actionEditRelationship.triggered.connect(self.selectEditRelationship)
        RelationshipContextMenuView.actionDeleteRelationship.triggered.connect(self.selectDeleteRelationship)

    def selectEditRelationship(self):
        self.isEditRelationshipSelected = True

    def unselectEditRelationship(self):
        self.isEditRelationshipSelected = False

    def getSelectEditRelationshipStatus(self):
        return self.isEditRelationshipSelected

    def selectDeleteRelationship(self):
        self.isDeleteRelationshipSelected = True

    def unselectDeleteRelationship(self):
        self.isDeleteRelationshipSelected = False

    def getSelectDeleteRelationshipStatus(self):
        return self.isDeleteRelationshipSelected
