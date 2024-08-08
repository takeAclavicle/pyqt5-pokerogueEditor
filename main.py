import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow

from resource_rc import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(':/pokemon/favicon.ico'))
    m = MainWindow()
    m.setFixedSize(m.width(), m.height())
    m.show()
    sys.exit(app.exec_())
