#learn how to create GUI with PyQT
# errors from the import statments dont seem to be true???

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys


class  Base(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(500, 500, 500, 320) #size of window
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('resources/icon.png'))        
    
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # window = MainWindow()
    # window.show()

    base = Base()
    sys.exit(app.exec_())