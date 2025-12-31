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
from app.controllers.ExportDiagramController import ExportDiagramController
from app.controllers.GenerateSQLController import GenerateSQLController
from app.models.TablesModel import TablesModel
from app.models.RelationshipsModel import RelationshipsModel
from app.models.InheritancesModel import InheritancesModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # views
        self.__MainWindowView = MainWindowView()
        self.__MainWindowView.setupUi(self)

        self.__ToolBarView = ToolBarView(self)
        self.__ToolBarView.setupUI()
        self.addToolBar(self.__ToolBarView)

        # controllers
        self.__ScrollAreaView = ScrollAreaView(self)
        self.__MainWindowController = MainWindowController(self.__MainWindowView)
        self.__ExportDialogController = ExportDiagramController(self, self.__ScrollAreaView)
        self.__DrawingAreaController = DrawingAreaController()

        # models
        self.__TablesModel = TablesModel()
        self.__RelationshipsModel = RelationshipsModel()
        self.__InheritancesModel = InheritancesModel()

        # views
        self.__GenerateSQLController = GenerateSQLController(self, self.__TablesModel, self.__RelationshipsModel,
                                                             self.__InheritancesModel)
        self.__ToolBarController = ToolBarController(self.__ToolBarView, self.__DrawingAreaController,
                                                     self.__ExportDialogController, self.__GenerateSQLController)
        self.__DrawingAreaView = DrawingAreaView(self.__DrawingAreaController)
        self.__ScrollAreaView.setupUI(self.__DrawingAreaView)
        self.__DrawingAreaView.setupUI()
        self.__MainWindowView.addCentralWidget(self.__ScrollAreaView)
        self.__TablesView = TablesView(self.__TablesModel, self.__DrawingAreaView)
        self.__RelationshipsView = RelationshipsView(self.__RelationshipsModel, self.__DrawingAreaView)
        self.__InheritancesView = InheritancesView(self.__InheritancesModel, self.__DrawingAreaView)

        # controllers
        self.__DrawingAreaController.setDrawingAreaView(self.__DrawingAreaView)
        self.__DrawingAreaController.setMainWindowController(self.__MainWindowController)
        self.__TablesController = TablesController(self, self.__TablesView, self.__TablesModel, self.__RelationshipsModel,
                                                   self.__InheritancesModel)
        self.__RelationshipsController = RelationshipsController(self, self.__RelationshipsView, self.__RelationshipsModel,
                                                                 self.__TablesModel)
        self.__InheritancesController = InheritancesController(self, self.__InheritancesView, self.__InheritancesModel,
                                                               self.__TablesModel)
        self.__DrawingAreaController.setToolBarController(self.__ToolBarController)
        self.__DrawingAreaController.setTablesController(self.__TablesController)
        self.__DrawingAreaController.setRelationshipsController(self.__RelationshipsController)
        self.__DrawingAreaController.setInheritancesController(self.__InheritancesController)

        # views
        self.__DrawingAreaView.setTablesModel(self.__TablesModel)
