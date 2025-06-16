class GenerateSQLDialogController:
    def __init__(self, GenerateSQLDialogView, TablesModel, RelationshipsModel, InheritancesModel):
        self.GenerateSQLDialogView = GenerateSQLDialogView
        self.TablesModel = TablesModel
        self.RelationshipsModel = RelationshipsModel
        self.InheritancesModel = InheritancesModel


