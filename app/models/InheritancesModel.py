from app.models.InheritanceModel import InheritanceModel


class InheritancesModel:
    def __init__(self):
        self.inheritances = []

    def addInheritance(self, FirstTable, SecondTable):
        CreatedInheritance = InheritanceModel(FirstTable, SecondTable)
        self.inheritances.append(CreatedInheritance)

    def clearInheritances(self):
        self.inheritances.clear()

    def getInheritances(self):
        return self.inheritances

    def deleteSelectedInheritances(self, SelectedInheritance):
        self.inheritances.remove(SelectedInheritance)

    def deleteInheritanceByTable(self, ObtainedTable):
        self.inheritances = [
            inheritance for inheritance in self.inheritances
            if inheritance.getFirstTable() is not ObtainedTable and inheritance.getSecondTable() is not ObtainedTable
        ]
