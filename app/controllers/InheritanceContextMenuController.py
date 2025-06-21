class InheritanceContextMenuController:
    def __init__(self, InheritanceContextMenuView):
        self.isEditInheritanceSelected = False
        self.isDeleteInheritanceSelected = False
        InheritanceContextMenuView.actionEditInheritance.triggered.connect(self.selectEditInheritance)
        InheritanceContextMenuView.actionDeleteInheritance.triggered.connect(self.selectDeleteInheritance)

    def selectEditInheritance(self):
        self.isEditInheritanceSelected = True

    def unselectEditInheritance(self):
        self.isEditInheritanceSelected = False

    def getSelectEditInheritanceStatus(self):
        return self.isEditInheritanceSelected

    def selectDeleteInheritance(self):
        self.isDeleteInheritanceSelected = True

    def unselectDeleteInheritance(self):
        self.isDeleteInheritanceSelected = False

    def getSelectDeleteInheritanceStatus(self):
        return self.isDeleteInheritanceSelected
