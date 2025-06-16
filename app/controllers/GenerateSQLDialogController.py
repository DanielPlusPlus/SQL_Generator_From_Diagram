from app.views.GenerateSQLDialogView import GenerateSQLDialogView


class GenerateSQLDialogController:
    def __init__(self, ParentWindow, TablesModel, RelationshipsModel, InheritancesModel):
        self.TablesModel = TablesModel
        self.RelationshipsModel = RelationshipsModel
        self.InheritancesModel = InheritancesModel
        self.GenerateSQLDialogView = GenerateSQLDialogView(ParentWindow)

    def displayDialog(self):
        self.GenerateSQLDialogView.setupUI()
        self.GenerateSQLDialogView.displayDialog()

