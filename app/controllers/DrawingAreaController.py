from PySide6.QtCore import Qt, QPoint

from app.enums.RelStatusEnum import RelStatusEnum
from app.enums.TableContextMenuEnum import TableContextMenuEnum


class DrawingAreaController:
    def __init__(self):
        self.DrawingAreaView = None
        self.cursorPosition = QPoint()
        self.MainWindowController = None
        self.ToolBarController = None
        self.TablesController = None
        self.RelationshipsController = None

    def setDrawingAreaView(self, DrawingAreaView):
        self.DrawingAreaView = DrawingAreaView

    def setMainWindowController(self, MainWindowController):
        self.MainWindowController = MainWindowController

    def setToolBarController(self, ToolBarController):
        self.ToolBarController = ToolBarController

    def setTablesController(self, TablesController):
        self.TablesController = TablesController

    def setRelationshipsController(self, RelationshipsController):
        self.RelationshipsController = RelationshipsController

    def handleMouseMove(self, event):
        self.cursorPosition = event.position().toPoint()
        self.MainWindowController.updateStatusBarInView(self.cursorPosition)

    def handleMousePress(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.ToolBarController.getCreateTableToolStatus():
                self.TablesController.addTable(self.cursorPosition)
                self.ToolBarController.unselectCreateTableTool()

            elif self.ToolBarController.getCreate_1_1_RelStatus() is RelStatusEnum.IN_MOTION_BEFORE_CLICK:
                if self.RelationshipsController.setFirstClickedTable(self.cursorPosition):
                    self.RelationshipsController.selectRelationshipBeingDrawn()
                    self.ToolBarController.changeStatusToAfterClick_1_1_Rel()
            elif self.ToolBarController.getCreate_1_1_RelStatus() is RelStatusEnum.IN_MOTION_AFTER_CLICK:
                if self.RelationshipsController.setSecondClickedTable(self.cursorPosition):
                    self.RelationshipsController.add_1_1_Relationship()
                    self.RelationshipsController.unselectRelationshipBeingDrawn()
                    self.ToolBarController.unselectCreate_1_1_Rel()

            elif self.ToolBarController.getCreate_1_n_RelStatus() is RelStatusEnum.IN_MOTION_BEFORE_CLICK:
                if self.RelationshipsController.setFirstClickedTable(self.cursorPosition):
                    self.RelationshipsController.selectRelationshipBeingDrawn()
                    self.ToolBarController.changeStatusToAfterClick_1_n_Rel()
            elif self.ToolBarController.getCreate_1_n_RelStatus() is RelStatusEnum.IN_MOTION_AFTER_CLICK:
                if self.RelationshipsController.setSecondClickedTable(self.cursorPosition):
                    self.RelationshipsController.add_1_n_Relationship()
                    self.RelationshipsController.unselectRelationshipBeingDrawn()
                    self.ToolBarController.unselectCreate_1_n_Rel()

            elif self.ToolBarController.getCreate_n_n_RelStatus() is RelStatusEnum.IN_MOTION_BEFORE_CLICK:
                if self.RelationshipsController.setFirstClickedTable(self.cursorPosition):
                    self.RelationshipsController.selectRelationshipBeingDrawn()
                    self.ToolBarController.changeStatusToAfterClick_n_n_Rel()
            elif self.ToolBarController.getCreate_n_n_RelStatus() is RelStatusEnum.IN_MOTION_AFTER_CLICK:
                if self.RelationshipsController.setSecondClickedTable(self.cursorPosition):
                    self.RelationshipsController.add_n_n_Relationship()
                    self.RelationshipsController.unselectRelationshipBeingDrawn()
                    self.ToolBarController.unselectCreate_n_n_Rel()

            elif self.TablesController.getTableInTransferStatus():
                self.TablesController.unselectTableInTransfer(self.cursorPosition)
            elif self.TablesController.getContextMenuAtWorkStatus():
                self.TablesController.unselectContextMenuAtWork()
            else:
                self.TablesController.selectTableInTransfer(self.cursorPosition)
        elif event.button() == Qt.MouseButton.RightButton:
            if self.ToolBarController.getCreateTableToolStatus():
                self.ToolBarController.unselectCreateTableTool()  # anulowanie rysowania (czy dobrze?)

            elif self.ToolBarController.getCreate_1_1_RelStatus() is not RelStatusEnum.NOT_IN_MOTION:
                self.RelationshipsController.unselectConnectionBeingDrawn()
                self.ToolBarController.unselectCreate_1_1_Rel()
            elif self.ToolBarController.getCreate_1_n_RelStatus() is not RelStatusEnum.NOT_IN_MOTION:
                self.RelationshipsController.unselectConnectionBeingDrawn()
                self.ToolBarController.unselectCreate_1_n_Rel()
            elif self.ToolBarController.getCreate_n_n_RelStatus() is not RelStatusEnum.NOT_IN_MOTION:
                self.RelationshipsController.unselectConnectionBeingDrawn()
                self.ToolBarController.unselectCreate_n_n_Rel()

            elif self.TablesController.getTableInTransferStatus():
                pass
            elif self.TablesController.getContextMenuAtWorkStatus():
                self.TablesController.unselectContextMenuAtWork()
            elif not self.TablesController.getContextMenuAtWorkStatus():
                globalCursorPosition = self.convertCursorPositionToGlobal(self.cursorPosition)
                result = self.TablesController.displayTableContextMenu(self.cursorPosition, globalCursorPosition)
                if result == TableContextMenuEnum.EDIT:
                    self.TablesController.editTable(self.cursorPosition)
                elif result == TableContextMenuEnum.DELETE:
                    self.TablesController.deleteTable(self.cursorPosition)

    def handlePaintEvent(self):
        if self.ToolBarController.getCreateTableToolStatus():
            self.TablesController.selectDrawTempTable(self.cursorPosition)
        elif self.TablesController.getTableInTransferStatus():
            self.TablesController.updateTableInTransferPosition(self.cursorPosition)
        elif self.RelationshipsController.getRelationshipBeingDrawnStatus():
            self.RelationshipsController.selectDrawRelationshipBeingDrawn(self.cursorPosition)
        self.TablesController.selectDrawTables()
        self.RelationshipsController.selectDrawRelationships()

    def convertCursorPositionToGlobal(self, cursorPosition):
        return self.DrawingAreaView.mapToGlobal(cursorPosition)
