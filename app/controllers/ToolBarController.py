from app.enums.ConnectionsStatusEnum import ConnectionsStatusEnum


class ToolBarController:
    def __init__(self, ToolBarView, DrawingAreaController, ExportDiagramController, GenerateSQLDialogController):
        self.DrawingAreaController = DrawingAreaController
        self.ExportDiagramController = ExportDiagramController
        self.GenerateSQLDialogController = GenerateSQLDialogController
        self.isTableSelected = False
        self.is_1_1_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.is_1_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.is_n_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.isInheritanceSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        ToolBarView.actionCreateTable.triggered.connect(self.selectCreateTableTool)
        ToolBarView.actionCreate_1_1_Rel.triggered.connect(self.selectCreate_1_1_RelTool)
        ToolBarView.actionCreate_1_n_Rel.triggered.connect(self.selectCreate_1_n_RelTool)
        ToolBarView.actionCreate_n_n_Rel.triggered.connect(self.selectCreate_n_n_RelTool)
        ToolBarView.actionCreateInheritance.triggered.connect(self.selectCreateInheritanceTool)
        ToolBarView.actionSaveDiagram.triggered.connect(self.selectSaveDiagramTool)
        ToolBarView.actionGenerateSQL.triggered.connect(self.selectGenerateSQLTool)
        # trzeba stworzyc anulowanie akcji

    def selectCreateTableTool(self):
        self.unselectAllTools()
        self.DrawingAreaController.unselectConnectionsBeingDrawn()
        self.DrawingAreaController.updateView()
        self.isTableSelected = True

    def unselectCreateTableTool(self):
        self.isTableSelected = False

    def getCreateTableToolStatus(self):
        return self.isTableSelected

    def selectCreate_1_1_RelTool(self):
        self.unselectAllTools()
        self.DrawingAreaController.unselectConnectionsBeingDrawn()
        self.DrawingAreaController.updateView()
        self.is_1_1_RelSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_1_1_RelTool(self):
        self.is_1_1_RelSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_1_1_RelTool(self):
        self.is_1_1_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreate_1_1_RelToolStatus(self):
        return self.is_1_1_RelSelected

    def selectCreate_1_n_RelTool(self):
        self.unselectAllTools()
        self.DrawingAreaController.unselectConnectionsBeingDrawn()
        self.DrawingAreaController.updateView()
        self.is_1_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_1_n_RelTool(self):
        self.is_1_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_1_n_RelTool(self):
        self.is_1_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreate_1_n_RelToolStatus(self):
        return self.is_1_n_RelSelected

    def selectCreate_n_n_RelTool(self):
        self.unselectAllTools()
        self.DrawingAreaController.unselectConnectionsBeingDrawn()
        self.DrawingAreaController.updateView()
        self.is_n_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_n_n_RelTool(self):
        self.is_n_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_n_n_RelTool(self):
        self.is_n_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreate_n_n_RelToolStatus(self):
        return self.is_n_n_RelSelected

    def selectCreateInheritanceTool(self):
        self.unselectAllTools()
        self.DrawingAreaController.unselectConnectionsBeingDrawn()
        self.DrawingAreaController.updateView()
        self.isInheritanceSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClickInheritanceTool(self):
        self.isInheritanceSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreateInheritanceTool(self):
        self.isInheritanceSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreateInheritanceToolStatus(self):
        return self.isInheritanceSelected

    def selectSaveDiagramTool(self):
        self.unselectAllTools()
        self.DrawingAreaController.unselectConnectionsBeingDrawn()
        self.DrawingAreaController.updateView()
        self.ExportDiagramController.exportDiagramToPNG()

    def selectGenerateSQLTool(self):
        self.unselectAllTools()
        self.DrawingAreaController.unselectConnectionsBeingDrawn()
        self.DrawingAreaController.updateView()
        self.GenerateSQLDialogController.displayDialog()

    def unselectAllTools(self):
        self.isTableSelected = False
        self.is_1_1_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.is_1_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.is_n_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION
        self.isInheritanceSelected = ConnectionsStatusEnum.NOT_IN_MOTION

