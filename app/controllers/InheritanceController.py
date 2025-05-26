from app.controllers.ConnectionsController import ConnectionsController


class RelationshipsController(ConnectionsController):
    def __init__(self, InheritanceView, InheritanceModel, TablesModel):
        super().__init__(TablesModel)
        self.InheritanceView = InheritanceView
        self.InheritanceModel = InheritanceModel
