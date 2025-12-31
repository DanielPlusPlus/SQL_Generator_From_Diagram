class MainWindowController:
    def __init__(self, MainWindowView):
        self.__MainWindowView = MainWindowView

    def updateStatusBarInView(self, position):
        message = "Current mouse position: x - " + str(position.x()) + ", y - " + str(position.y())
        self.__MainWindowView.updateStatusBar(message)
