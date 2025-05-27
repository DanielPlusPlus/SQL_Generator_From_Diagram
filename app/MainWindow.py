from PySide6.QtWidgets import QMainWindow

from app.views.MainWindowView import MainWindowView
from app.views.ToolBarView import ToolBarView
from app.views.ScrollAreaView import ScrollAreaView
from app.views.DrawingAreaView import DrawingAreaView
from app.views.TablesView import TablesView
from app.views.RelationshipsView import RelationshipsView
from app.views.InheritancesView import InheritancesView
from app.controllers.MainWindowController import MainWindowController
from app.controllers.ToolBarController import ToolBarController
from app.controllers.DrawingAreaController import DrawingAreaController
from app.controllers.TablesController import TablesController
from app.controllers.RelationshipsController import RelationshipsController
from app.controllers.InheritancesController import InheritancesController
from app.models.TablesModel import TablesModel
from app.models.RelationshipsModel import RelationshipsModel
from app.models.InheritancesModel import InheritancesModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # views
        self.MainWindowView = MainWindowView()
        self.MainWindowView.setupUi(self)

        self.ToolBarView = ToolBarView(self)
        self.ToolBarView.setupUI()
        self.addToolBar(self.ToolBarView)

        # controllers
        self.MainWindowController = MainWindowController(self.MainWindowView)
        self.ToolBarController = ToolBarController(self.ToolBarView)
        self.DrawingAreaController = DrawingAreaController()

        # models
        self.TablesModel = TablesModel()
        self.RelationshipsModel = RelationshipsModel()
        self.InheritancesModel = InheritancesModel()

        # views
        self.ScrollAreaView = ScrollAreaView(self)
        self.DrawingAreaView = DrawingAreaView(self.DrawingAreaController)
        self.ScrollAreaView.setupUI(self.DrawingAreaView)
        self.DrawingAreaView.setupUI()
        self.MainWindowView.addCentralWidget(self.ScrollAreaView)
        self.TablesView = TablesView(self.TablesModel, self.DrawingAreaView)
        self.RelationshipsView = RelationshipsView(self.RelationshipsModel, self.DrawingAreaView)
        self.InheritancesView = InheritancesView(self.InheritancesModel, self.DrawingAreaView)

        # controllers
        self.DrawingAreaController.setDrawingAreaView(self.DrawingAreaView)
        self.DrawingAreaController.setMainWindowController(self.MainWindowController)
        self.TablesController = TablesController(self, self.TablesView, self.TablesModel, self.RelationshipsModel,
                                                 self.InheritancesModel)
        self.RelationshipsController = RelationshipsController(self.RelationshipsView, self.RelationshipsModel,
                                                               self.TablesModel)
        self.InheritancesController = InheritancesController(self.InheritancesView, self.InheritancesModel,
                                                             self.TablesModel)
        self.DrawingAreaController.setToolBarController(self.ToolBarController)
        self.DrawingAreaController.setTablesController(self.TablesController)
        self.DrawingAreaController.setRelationshipsController(self.RelationshipsController)
        self.DrawingAreaController.setInheritancesController(self.InheritancesController)

        # views
        self.DrawingAreaView.setTablesModel(self.TablesModel)
