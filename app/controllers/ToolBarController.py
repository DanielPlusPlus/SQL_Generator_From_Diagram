from app.enums.RelStatusEnum import RelStatusEnum


class ToolBarController:
    def __init__(self, ToolBarView):
        self.isTableSelected = False
        self.is_1_1_RelSelected = RelStatusEnum.NOT_IN_MOTION
        self.is_1_n_RelSelected = RelStatusEnum.NOT_IN_MOTION
        self.is_n_n_RelSelected = RelStatusEnum.NOT_IN_MOTION
        ToolBarView.actionCreateTable.triggered.connect(self.selectCreateTableTool)
        ToolBarView.actionCreate_1_1_Rel.triggered.connect(self.selectCreate_1_1_Rel)
        ToolBarView.actionCreate_1_n_Rel.triggered.connect(self.selectCreate_1_n_Rel)
        ToolBarView.actionCreate_n_n_Rel.triggered.connect(self.selectCreate_n_n_Rel)
        ToolBarView.actionSaveDiagram.triggered.connect(self.selectSaveDiagram)
        ToolBarView.actionGenerateSQL.triggered.connect(self.selectGenerateSQL)
        # trzeba stworzyc anulowanie akcji

    def selectCreateTableTool(self):
        self.isTableSelected = True

    def unselectCreateTableTool(self):
        self.isTableSelected = False

    def getCreateTableToolStatus(self):
        return self.isTableSelected

    def selectCreate_1_1_Rel(self):
        self.is_1_1_RelSelected = RelStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_1_1_Rel(self):
        self.is_1_1_RelSelected = RelStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_1_1_Rel(self):
        self.is_1_1_RelSelected = RelStatusEnum.NOT_IN_MOTION

    def getCreate_1_1_RelStatus(self):
        return self.is_1_1_RelSelected

    def selectCreate_1_n_Rel(self):
        self.is_1_n_RelSelected = RelStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_1_n_Rel(self):
        self.is_1_n_RelSelected = RelStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_1_n_Rel(self):
        self.is_1_n_RelSelected = RelStatusEnum.NOT_IN_MOTION

    def getCreate_1_n_RelStatus(self):
        return self.is_1_n_RelSelected

    def selectCreate_n_n_Rel(self):
        self.is_n_n_RelSelected = RelStatusEnum.IN_MOTION_BEFORE_CLICK

    def changeStatusToAfterClick_n_n_Rel(self):
        self.is_n_n_RelSelected = RelStatusEnum.IN_MOTION_AFTER_CLICK

    def unselectCreate_n_n_Rel(self):
        self.is_n_n_RelSelected = RelStatusEnum.NOT_IN_MOTION

    def getCreate_n_n_RelStatus(self):
        return self.is_n_n_RelSelected

    def selectSaveDiagram(self):
        print("Selected save diagram tool")

    def selectGenerateSQL(self):
        print("Selected generate SQL tool")
