import cutter
from PySide2.QtWidgets import QAction, QFileDialog
from traceback import format_exc

class CutterPythonPlugin(cutter.CutterPlugin):
    name = "CutterPython"
    description = "Executes Python script for Cutter"
    version = "1.0"
    author = "CheckReverse"

    def setupPlugin(self):
        pass

    def setupInterface(self, main):
        action = QAction("CutterPython", main)
        action.setCheckable(False)
        action.setShortcut("Alt+F7")
        action.triggered.connect(self.executor)
        pluginsMenu = main.getMenuByType(main.MenuType.Plugins)
        pluginsMenu.addAction(action)

    def terminate(self):
        pass
    
    def executor(self):
        try:
            Filename=QFileDialog.getOpenFileName(caption="Select Python Script", filter="Python Script (*.py)")[0]
            with open(Filename, "r") as f:
                rBuffer=f.read()
            exec(rBuffer, globals())
        except Exception as e:
            cutter.message("[!] Script Error!")
            cutter.message(format_exc())
            
def create_cutter_plugin():
    return CutterPythonPlugin()
