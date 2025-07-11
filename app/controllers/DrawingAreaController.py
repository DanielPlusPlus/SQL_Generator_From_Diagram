from PySide6.QtCore import Qt, QPoint

from app.enums.ConnectionsStatusEnum import ConnectionsStatusEnum
from app.enums.TableContextMenuEnum import TableContextMenuEnum
from app.enums.RelationshipContextMenuEnum import RelationshipContextMenuEnum
from app.enums.InheritanceContextMenuEnum import InheritanceContextMenuEnum


class DrawingAreaController:
    def __init__(self):
        self.DrawingAreaView = None
        self.cursorPosition = QPoint()
        self.MainWindowController = None
        self.ToolBarController = None
        self.TablesController = None
        self.RelationshipsController = None
        self.InheritancesController = None

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

    def setInheritancesController(self, InheritancesController):
        self.InheritancesController = InheritancesController

    def handleMouseMove(self, event):
        self.cursorPosition = event.position().toPoint()
        self.MainWindowController.updateStatusBarInView(self.cursorPosition)

    def handleMousePress(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.ToolBarController.getCreateTableToolStatus():
                self.TablesController.addTable(self.cursorPosition)
                self.ToolBarController.unselectCreateTableTool()

            elif (self.ToolBarController.getCreate_1_1_RelToolStatus()
                  is ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK):
                if self.RelationshipsController.setFirstClickedTable(self.cursorPosition):
                    if self.RelationshipsController.setFirstSelectedColumnName():
                        self.ToolBarController.changeStatusToAfterClick_1_1_RelTool()
                        self.RelationshipsController.selectRelationshipBeingDrawn()
            elif (self.ToolBarController.getCreate_1_1_RelToolStatus()
                  is ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK):
                if self.RelationshipsController.setSecondClickedTable(self.cursorPosition):
                    if self.RelationshipsController.setSecondSelectedColumnName():
                        self.RelationshipsController.add_1_1_Relationship()
                        self.ToolBarController.unselectCreate_1_1_RelTool()
                        self.RelationshipsController.unselectRelationshipBeingDrawn()

            elif (self.ToolBarController.getCreate_1_n_RelToolStatus()
                  is ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK):
                if self.RelationshipsController.setFirstClickedTable(self.cursorPosition):
                    if self.RelationshipsController.setFirstSelectedColumnName():
                        self.ToolBarController.changeStatusToAfterClick_1_n_RelTool()
                        self.RelationshipsController.selectRelationshipBeingDrawn()
            elif (self.ToolBarController.getCreate_1_n_RelToolStatus()
                  is ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK):
                if self.RelationshipsController.setSecondClickedTable(self.cursorPosition):
                    if self.RelationshipsController.setSecondSelectedColumnName():
                        self.RelationshipsController.add_1_n_Relationship()
                        self.ToolBarController.unselectCreate_1_n_RelTool()
                        self.RelationshipsController.unselectRelationshipBeingDrawn()

            elif (self.ToolBarController.getCreate_n_n_RelToolStatus()
                  is ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK):
                if self.RelationshipsController.setFirstClickedTable(self.cursorPosition):
                    if self.RelationshipsController.setFirstSelectedColumnName():
                        self.ToolBarController.changeStatusToAfterClick_n_n_RelTool()
                        self.RelationshipsController.selectRelationshipBeingDrawn()
            elif (self.ToolBarController.getCreate_n_n_RelToolStatus()
                  is ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK):
                if self.RelationshipsController.setSecondClickedTable(self.cursorPosition):
                    if self.RelationshipsController.setSecondSelectedColumnName():
                        self.RelationshipsController.add_n_n_Relationship()
                        self.ToolBarController.unselectCreate_n_n_RelTool()
                        self.RelationshipsController.unselectRelationshipBeingDrawn()

            elif (self.ToolBarController.getCreateInheritanceToolStatus()
                  is ConnectionsStatusEnum.IN_MOTION_BEFORE_CLICK):
                if self.InheritancesController.setFirstClickedTable(self.cursorPosition):
                    self.ToolBarController.changeStatusToAfterClickInheritanceTool()
                    self.InheritancesController.selectInheritanceBeingDrawn()
            elif (self.ToolBarController.getCreateInheritanceToolStatus()
                  is ConnectionsStatusEnum.IN_MOTION_AFTER_CLICK):
                if self.InheritancesController.setSecondClickedTable(self.cursorPosition):
                    self.InheritancesController.addInheritance()
                    self.ToolBarController.unselectCreateInheritanceTool()
                    self.InheritancesController.unselectInheritanceBeingDrawn()

            elif self.TablesController.getTableInTransferStatus():
                self.TablesController.unselectTableInTransfer(self.cursorPosition)
            elif self.TablesController.getContextMenuAtWorkStatus():
                self.TablesController.unselectContextMenuAtWork()
            elif self.RelationshipsController.getContextMenuAtWorkStatus():
                self.RelationshipsController.unselectContextMenuAtWork()
            else:
                self.TablesController.selectTableInTransfer(self.cursorPosition)
        elif event.button() == Qt.MouseButton.RightButton:
            if self.ToolBarController.getCreateTableToolStatus():
                self.ToolBarController.unselectCreateTableTool()  # anulowanie rysowania (czy dobrze?)

            elif (self.ToolBarController.getCreate_1_1_RelToolStatus()
                  is not ConnectionsStatusEnum.NOT_IN_MOTION):
                self.RelationshipsController.unselectRelationshipBeingDrawn()
                self.ToolBarController.unselectCreate_1_1_RelTool()
            elif (self.ToolBarController.getCreate_1_n_RelToolStatus()
                  is not ConnectionsStatusEnum.NOT_IN_MOTION):
                self.RelationshipsController.unselectRelationshipBeingDrawn()
                self.ToolBarController.unselectCreate_1_n_RelTool()
            elif (self.ToolBarController.getCreate_n_n_RelToolStatus()
                  is not ConnectionsStatusEnum.NOT_IN_MOTION):
                self.RelationshipsController.unselectRelationshipBeingDrawn()
                self.ToolBarController.unselectCreate_n_n_RelTool()
            elif (self.ToolBarController.getCreateInheritanceToolStatus()
                  is not ConnectionsStatusEnum.NOT_IN_MOTION):
                self.InheritancesController.unselectInheritanceBeingDrawn()
                self.ToolBarController.unselectCreateInheritanceTool()

            elif self.TablesController.getTableInTransferStatus():
                pass
            elif self.TablesController.getContextMenuAtWorkStatus():
                self.TablesController.unselectContextMenuAtWork()
            elif self.RelationshipsController.getContextMenuAtWorkStatus():
                self.RelationshipsController.unselectContextMenuAtWork()
            elif (not self.TablesController.getContextMenuAtWorkStatus()
                  and not self.RelationshipsController.getContextMenuAtWorkStatus()
                  and not self.InheritancesController.getContextMenuAtWorkStatus()):
                globalCursorPosition = self.convertCursorPositionToGlobal(self.cursorPosition)
                result = self.TablesController.displayTableContextMenu(self.cursorPosition,
                                                                       globalCursorPosition)
                if result is TableContextMenuEnum.EDIT:
                    self.TablesController.editTable(self.cursorPosition)
                elif result is TableContextMenuEnum.DELETE:
                    self.TablesController.deleteTable(self.cursorPosition)
                else:
                    result = self.RelationshipsController.displayRelationshipContextMenu(self.cursorPosition,
                                                                                         globalCursorPosition)
                    if result is RelationshipContextMenuEnum.EDIT:
                        self.RelationshipsController.editRelationship(self.cursorPosition)
                    elif result is RelationshipContextMenuEnum.DELETE:
                        self.RelationshipsController.deleteRelationship(self.cursorPosition)

                    result = self.InheritancesController.displayInheritanceContextMenu(self.cursorPosition,
                                                                                       globalCursorPosition)
                    if result is InheritanceContextMenuEnum.EDIT:
                        self.InheritancesController.editInheritance(self.cursorPosition)
                    elif result is InheritanceContextMenuEnum.DELETE:
                        self.InheritancesController.deleteInheritance(self.cursorPosition)

    def handlePaintEvent(self):
        if self.ToolBarController.getCreateTableToolStatus():
            self.TablesController.selectDrawTempTable(self.cursorPosition)
        elif self.TablesController.getTableInTransferStatus():
            self.TablesController.updateTableInTransferPosition(self.cursorPosition)
        elif self.RelationshipsController.getRelationshipBeingDrawnStatus():
            self.RelationshipsController.selectDrawRelationshipBeingDrawn(self.cursorPosition)
        elif self.InheritancesController.getInheritanceBeingDrawnStatus():
            self.InheritancesController.selectDrawInheritanceBeingDrawn(self.cursorPosition)
        self.TablesController.selectDrawTables()
        self.RelationshipsController.selectDrawRelationships()
        self.InheritancesController.selectDrawInheritances()

    def convertCursorPositionToGlobal(self, cursorPosition):
        return self.DrawingAreaView.mapToGlobal(cursorPosition)

    def updateView(self):
        self.DrawingAreaView.update()

    def unselectConnectionsBeingDrawn(self):
        self.RelationshipsController.unselectRelationshipBeingDrawn()
        self.InheritancesController.unselectInheritanceBeingDrawn()
