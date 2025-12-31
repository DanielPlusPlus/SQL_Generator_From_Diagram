from app.enums.ConnectionsStatusEnum import ConnectionsStatusEnum


class ToolBarController:
    def __init__(self, ToolBarView, DrawingAreaController, ExportDiagramController, GenerateSQLDialogController):
        self.__DrawingAreaController = DrawingAreaController
        self.__ExportDiagramController = ExportDiagramController
        self.__GenerateSQLDialogController = GenerateSQLDialogController
        self.__isTableSelected = False
        self.__is_1_1_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.__is_1_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.__is_n_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.__isInheritanceSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        ToolBarView.actionCreateTable.triggered.connect(self.__selectCreateTableTool)
        ToolBarView.actionCreate_1_1_Rel.triggered.connect(self.__selectCreate_1_1_RelTool)
        ToolBarView.actionCreate_1_n_Rel.triggered.connect(self.__selectCreate_1_n_RelTool)
        ToolBarView.actionCreate_n_n_Rel.triggered.connect(self.__selectCreate_n_n_RelTool)
        ToolBarView.actionCreateInheritance.triggered.connect(self.__selectCreateInheritanceTool)
        ToolBarView.actionSaveDiagram.triggered.connect(self.__selectSaveDiagramTool)
        ToolBarView.actionGenerateSQL.triggered.connect(self.__selectGenerateSQLTool)
        # trzeba stworzyc anulowanie akcji

    def __selectCreateTableTool(self):
        self.__unselectAllTools()
        self.__DrawingAreaController.unselectConnectionsBeingDrawn()
        self.__DrawingAreaController.updateView()
        self.__isTableSelected = True

    def unselectCreateTableTool(self):
        self.__isTableSelected = False

    def getCreateTableToolStatus(self):
        return self.__isTableSelected

    def __selectCreate_1_1_RelTool(self):
        self.__unselectAllTools()
        self.__DrawingAreaController.unselectConnectionsBeingDrawn()
        self.__DrawingAreaController.updateView()
        self.__is_1_1_RelSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_1_1_RelTool(self):
        self.__is_1_1_RelSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_1_1_RelTool(self):
        self.__is_1_1_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreate_1_1_RelToolStatus(self):
        return self.__is_1_1_RelSelected

    def __selectCreate_1_n_RelTool(self):
        self.__unselectAllTools()
        self.__DrawingAreaController.unselectConnectionsBeingDrawn()
        self.__DrawingAreaController.updateView()
        self.__is_1_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_1_n_RelTool(self):
        self.__is_1_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_1_n_RelTool(self):
        self.__is_1_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreate_1_n_RelToolStatus(self):
        return self.__is_1_n_RelSelected

    def __selectCreate_n_n_RelTool(self):
        self.__unselectAllTools()
        self.__DrawingAreaController.unselectConnectionsBeingDrawn()
        self.__DrawingAreaController.updateView()
        self.__is_n_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_n_n_RelTool(self):
        self.__is_n_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_n_n_RelTool(self):
        self.__is_n_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreate_n_n_RelToolStatus(self):
        return self.__is_n_n_RelSelected

    def __selectCreateInheritanceTool(self):
        self.__unselectAllTools()
        self.__DrawingAreaController.unselectConnectionsBeingDrawn()
        self.__DrawingAreaController.updateView()
        self.__isInheritanceSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClickInheritanceTool(self):
        self.__isInheritanceSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreateInheritanceTool(self):
        self.__isInheritanceSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreateInheritanceToolStatus(self):
        return self.__isInheritanceSelected

    def __selectSaveDiagramTool(self):
        self.__unselectAllTools()
        self.__DrawingAreaController.unselectConnectionsBeingDrawn()
        self.__DrawingAreaController.updateView()
        self.__ExportDiagramController.exportDiagramToPNG()

    def __selectGenerateSQLTool(self):
        self.__unselectAllTools()
        self.__DrawingAreaController.unselectConnectionsBeingDrawn()
        self.__DrawingAreaController.updateView()
        self.__GenerateSQLDialogController.displayDialog()

    def __unselectAllTools(self):
        self.__isTableSelected = False
        self.__is_1_1_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.__is_1_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.__is_n_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.__isInheritanceSelected = ConnectionsStatusEnum.NOT_IN_MOTION

