class InheritanceContextMenuController:
    def __init__(self, InheritanceContextMenuView):
        self.__isEditInheritanceSelected = False
        self.__isDeleteInheritanceSelected = False
        InheritanceContextMenuView.actionEditInheritance.triggered.connect(self.__selectEditInheritance)
        InheritanceContextMenuView.actionDeleteInheritance.triggered.connect(self.__selectDeleteInheritance)

    def __selectEditInheritance(self):
        self.__isEditInheritanceSelected = True

    def unselectEditInheritance(self):
        self.__isEditInheritanceSelected = False

    def getSelectEditInheritanceStatus(self):
        return self.__isEditInheritanceSelected

    def __selectDeleteInheritance(self):
        self.__isDeleteInheritanceSelected = True

    def unselectDeleteInheritance(self):
        self.__isDeleteInheritanceSelected = False

    def getSelectDeleteInheritanceStatus(self):
        return self.__isDeleteInheritanceSelected
