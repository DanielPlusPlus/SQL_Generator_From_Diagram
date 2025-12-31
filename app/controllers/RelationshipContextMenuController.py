class RelationshipContextMenuController:
    def __init__(self, RelationshipContextMenuView):
        self.__isEditRelationshipSelected = False
        self.__isDeleteRelationshipSelected = False
        RelationshipContextMenuView.actionEditRelationship.triggered.connect(self.__selectEditRelationship)
        RelationshipContextMenuView.actionDeleteRelationship.triggered.connect(self.__selectDeleteRelationship)

    def __selectEditRelationship(self):
        self.__isEditRelationshipSelected = True

    def unselectEditRelationship(self):
        self.__isEditRelationshipSelected = False

    def getSelectEditRelationshipStatus(self):
        return self.__isEditRelationshipSelected

    def __selectDeleteRelationship(self):
        self.__isDeleteRelationshipSelected = True

    def unselectDeleteRelationship(self):
        self.__isDeleteRelationshipSelected = False

    def getSelectDeleteRelationshipStatus(self):
        return self.__isDeleteRelationshipSelected
