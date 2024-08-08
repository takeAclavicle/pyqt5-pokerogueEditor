import sys
from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QLineEdit, QListView
from PyQt5.QtCore import Qt, QModelIndex


class MultiComboBox(QComboBox):
    def __init__(self, parent=None):
        super(MultiComboBox, self).__init__(parent)
        self.setView(QListView())
        self.setLineEdit(QLineEdit())
        self.lineEdit().setReadOnly(True)
        self.view().clicked.connect(self.selectItemAction)
        self.setStyleSheet('QAbstractItemView::item {height:%dpx;}' % (self.height() * 3 // 4))
        self.SelectAllStatus = 0
        self.init()

    def init(self):
        self.SelectAllStatus = 0
        self.addMultiItem('全选', 0)
        self.setCurrentIndex(-1)

    def addMultiItem(self, *args):
        if len(args) == 1:
            super().addItem(args[0])
        else:
            super().addItem(args[0], args[1])

        item = self.model().item(self.count() - 1, 0)
        item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
        item.setCheckState(Qt.CheckState.Unchecked)

    def addMultiItems(self, text_list):
        for text in text_list:
            self.addMultiItem(text)

    def isChecked(self, index):
        item = self.model().item(index, 0)
        return item.checkState() == Qt.CheckState.Checked

    def checkedIndexes(self):
        return [i for i in range(self.count()) if self.isChecked(i)]

    def checkedItems(self):
        return [self.itemText(i) for i in range(self.count()) if self.isChecked(i)]

    def checkedStr(self):
        if self.SelectAllStatus == 1:
            return '全选'

        checkedItems = self.checkedItems()
        if len(checkedItems) == self.count() - 1:
            self.SelectAllStatus = 1
            self.model().item(0).setCheckState(Qt.CheckState.Checked)
            return '全选'
        return ';'.join(checkedItems)

    def showPopup(self):
        super().showPopup()

    def selectItemAction(self, index: QModelIndex):
        if index.row() == 0:
            self.SelectAllStatus = (self.SelectAllStatus + 1) % 2
            if self.SelectAllStatus:
                for i in range(self.count()):
                    self.model().item(i).setCheckState(Qt.CheckState.Checked)
            else:
                for i in range(self.count()):
                    self.model().item(i).setCheckState(Qt.CheckState.Unchecked)
        else:
            if self.SelectAllStatus:
                self.model().item(0).setCheckState(Qt.CheckState.Unchecked)
                self.SelectAllStatus = 0

        self.lineEdit().setText(self.checkedStr())

    def clear(self) -> None:
        super().clear()
        self.init()

    def select_all(self):
        for i in range(self.model().rowCount()):
            self.model().item(i).setCheckState(Qt.CheckState.Checked)
        self.lineEdit().setText(self.checkedStr())


from ui_mainwindow import Ui_MainWindow


class Ui_Study(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.resize(300,500)
        # self.comboBox_starterNatures.move(20, 20)
        # self.comboBox_starterNatures.resize(200, 30)

        # self.line_edit = QLineEdit(self)
        # self.line_edit.move(20, 80)
        # self.line_edit.resize(300, 30)

        self.comboBox_starterNatures.addMultiItem("qf1", 2)
        self.comboBox_starterNatures.addMultiItem("qf2", 4)
        self.comboBox_starterNatures.addMultiItem("qf3", 8)
        self.comboBox_starterNatures.addMultiItem("qf4", 16)
        self.comboBox_starterNatures.addMultiItem("qf1", 2)
        self.comboBox_starterNatures.addMultiItem("qf2", 4)
        self.comboBox_starterNatures.addMultiItem("qf3", 8)
        self.comboBox_starterNatures.addMultiItem("qf4", 16)
        self.comboBox_starterNatures.addMultiItem("qf4", 16)
        self.comboBox_starterNatures.addMultiItem("qf1", 2)
        self.comboBox_starterNatures.addMultiItem("qf2", 4)
        self.comboBox_starterNatures.addMultiItem("qf3", 8)
        self.comboBox_starterNatures.addMultiItem("qf4", 16)
        self.comboBox_starterNatures.addMultiItem("qf3", 8)
        self.comboBox_starterNatures.addMultiItem("qf4", 16)
        self.comboBox_starterNatures.addMultiItem("qf4", 16)
        self.comboBox_starterNatures.addMultiItem("qf1", 2)
        self.comboBox_starterNatures.addMultiItem("qf2", 4)
        self.comboBox_starterNatures.addMultiItem("qf3", 8)
        self.comboBox_starterNatures.addMultiItem("qf4", 16)
        # self.combobox.lineEdit().textChanged.connect(lambda: self.line_edit.setText(self.combobox.checkedItemsStr()))
        self.comboBox_nature.addItem("qf1", 2)
        self.comboBox_nature.addItem("qf2", 4)
        self.comboBox_nature.addItem("qf3", 8)
        self.comboBox_nature.addItem("qf4", 16)
        self.comboBox_nature.addItem("qf1", 2)
        self.comboBox_nature.addItem("qf2", 4)
        self.comboBox_nature.addItem("qf3", 8)
        self.comboBox_nature.addItem("qf4", 16)
        self.comboBox_nature.addItem("qf4", 16)
        self.comboBox_nature.addItem("qf1", 2)
        self.comboBox_nature.addItem("qf2", 4)
        self.comboBox_nature.addItem("qf3", 8)
        self.comboBox_nature.addItem("qf4", 16)
        self.comboBox_nature.addItem("qf3", 8)
        self.comboBox_nature.addItem("qf4", 16)
        self.comboBox_nature.addItem("qf4", 16)
        self.comboBox_nature.addItem("qf1", 2)
        self.comboBox_nature.addItem("qf2", 4)
        self.comboBox_nature.addItem("qf3", 8)
        self.comboBox_nature.addItem("qf4", 16)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_ui = Ui_Study()
    print(my_ui.comboBox_nature.itemData(4))
    # a = my_ui.combobox
    sys.exit(app.exec())
