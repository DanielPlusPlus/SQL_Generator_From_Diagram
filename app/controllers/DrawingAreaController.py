from PySide6.QtCore import Qt, QPoint

from app.enums.RelStatusEnum import RelStatusEnum
from app.enums.TableContextMenuEnum import TableContextMenuEnum


# trzy listy w modelu,

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

            elif self.ToolBarController.getCreate_1_1_RelStatus() == RelStatusEnum.IN_MOTION_BEFORE_CLICK:
                self.RelationshipsController.setFirstClickedTable(self.cursorPosition)
                self.ToolBarController.changeStatusToAfterClick()
            elif self.ToolBarController.getCreate_1_1_RelStatus() == RelStatusEnum.IN_MOTION_AFTER_CLICK:
                self.RelationshipsController.setSecondClickedTable(self.cursorPosition)
                self.RelationshipsController.add_1_1_Relationship()
                self.ToolBarController.unselectCreate_1_1_Rel()

            elif self.TablesController.getTableInTransferStatus():
                self.TablesController.unselectTableInTransfer(self.cursorPosition)
            elif self.TablesController.getContextMenuAtWorkStatus():
                self.TablesController.unselectContextMenuAtWork()
            else:
                self.TablesController.selectTableInTransfer(self.cursorPosition)
        elif event.button() == Qt.MouseButton.RightButton:
            if self.ToolBarController.getCreateTableToolStatus():
                self.ToolBarController.unselectCreateTableTool()  # anulowanie rysowania (czy dobrze?)
            elif self.TablesController.getTableInTransferStatus():
                pass
            else:
                globalCursorPosition = self.DrawingAreaView.convertCursorPositionToGlobal(self.cursorPosition)
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
        self.TablesController.selectDrawTables()
        self.RelationshipsController.selectDrawRelationships()
