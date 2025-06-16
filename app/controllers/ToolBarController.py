from app.enums.ConnectionsStatusEnum import ConnectionsStatusEnum


class ToolBarController:
    def __init__(self, ToolBarView, ExportDiagramController):
        self.ExportDiagramController = ExportDiagramController
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
        ToolBarView.actionSaveDiagram.triggered.connect(self.selectSaveDiagram)
        ToolBarView.actionGenerateSQL.triggered.connect(self.selectGenerateSQL)
        # trzeba stworzyc anulowanie akcji

    def selectCreateTableTool(self):
        self.isTableSelected = True

    def unselectCreateTableTool(self):
        self.isTableSelected = False

    def getCreateTableToolStatus(self):
        return self.isTableSelected

    def selectCreate_1_1_RelTool(self):
        self.is_1_1_RelSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_1_1_RelTool(self):
        self.is_1_1_RelSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_1_1_RelTool(self):
        self.is_1_1_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreate_1_1_RelToolStatus(self):
        return self.is_1_1_RelSelected

    def selectCreate_1_n_RelTool(self):
        self.is_1_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_1_n_RelTool(self):
        self.is_1_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_1_n_RelTool(self):
        self.is_1_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreate_1_n_RelToolStatus(self):
        return self.is_1_n_RelSelected

    def selectCreate_n_n_RelTool(self):
        self.is_n_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_n_n_RelTool(self):
        self.is_n_n_RelSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_n_n_RelTool(self):
        self.is_n_n_RelSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreate_n_n_RelToolStatus(self):
        return self.is_n_n_RelSelected

    def selectCreateInheritanceTool(self):
        self.isInheritanceSelected = ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClickInheritanceTool(self):
        self.isInheritanceSelected = ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreateInheritanceTool(self):
        self.isInheritanceSelected = ConnectionsStatusEnum.NOT_IN_MOTION

    def getCreateInheritanceToolStatus(self):
        return self.isInheritanceSelected

    def selectSaveDiagram(self):
        self.ExportDiagramController.exportDiagramToPNG()

    def selectGenerateSQL(self):
        pass
