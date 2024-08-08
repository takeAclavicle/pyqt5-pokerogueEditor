import json
import os
import datetime

from PyQt5.QtCore import pyqtSlot, Qt, QSize
from PyQt5.QtGui import QIcon, QPainter, QColor, QPixmap, QTransform
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QListWidget, QListView, QListWidgetItem, QVBoxLayout, QAbstractItemView, QPushButton, QMessageBox
from ui_mainwindow import Ui_MainWindow
from racer_crypt import Cryptor

from KEY_DICT import *
from itemLogic import ModifierType

from random import randint
from resource_rc import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cryptor = Cryptor('x0i2O7WRiANTqPmZ')
        self.select_partner: dict = {}
        self.LWidgetGen: list[QListWidget] = []
        self.initUI()
        self.setAcceptDrops(True)

        # pix = QPixmap('png/ability_charm.png')
        # painter = QPainter(pix)
        # painter.setPen(Qt.black)
        #
        # font = painter.font()
        # font.setPixelSize(11)
        # font.setFamily("Microsoft YaHei")
        # painter.setFont(font)
        #
        # painter.drawText(pix.rect(), Qt.AlignRight | Qt.AlignBottom, '11')
        # painter.end()
        # pListItem = QListWidgetItem(QIcon(pix), '')
        # pListItem.setSizeHint(QSize(pix.width(), pix.height()))
        # self.listWidget_party_item.addItem(pListItem)

    def initUI(self):
        self.listWidget.setSpacing(5)
        self.pushButton_1.clicked.connect(self.slot_switch)
        self.pushButton_2.clicked.connect(self.slot_switch)
        self.pushButton_3.clicked.connect(self.slot_switch)
        self.pushButton_4.clicked.connect(self.slot_switch)
        self.pushButton_5.clicked.connect(self.slot_switch)
        self.pushButton_6.clicked.connect(self.slot_switch)
        self.pushButton_7.clicked.connect(self.slot_switch)
        self.pushButton_8.clicked.connect(self.slot_switch)
        self.pushButton_9.clicked.connect(self.slot_switch)

        for i in range(0, 9):
            VLayGen = QVBoxLayout(self.stackedWidget.widget(i))
            self.LWidgetGen.append(QListWidget())
            self.LWidgetGen[i].setMovement(QListView.Static)
            self.LWidgetGen[i].setViewMode(QListView.IconMode)
            self.LWidgetGen[i].setSelectionMode(QAbstractItemView.MultiSelection)
            self.LWidgetGen[i].setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.LWidgetGen[i].setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            VLayGen.addWidget(self.LWidgetGen[i])

        widgets = [self.listWidget, self.listWidget_party_item]
        for w in widgets:
            w.setMovement(QListView.Static)
            w.setViewMode(QListView.IconMode)
            w.setSelectionMode(QAbstractItemView.SingleSelection)
            w.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            w.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.comboBox_ability.addItems(['特性1', '特性2', '梦特性'])
        ui_moves = [self.comboBox_move_1, self.comboBox_move_2, self.comboBox_move_3, self.comboBox_move_4]
        for ui in ui_moves:
            for id, zh in move_dict.items():
                ui.addItem(zh, id)
        for k, v in bio_dict.items():
            self.comboBox_biome.addItem(v, k)

        list_widget = QListWidget()
        list_widget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        for zh, value in nature_dict.items():
            self.comboBox_starterNatures.addMultiItem(zh, value)
            self.comboBox_nature.addItem(zh)

    def readFile(self, filepath):
        if filepath[-4:] not in ['prsv', 'json']:
            QMessageBox.critical(self, "错误", "请选择正确的文件格式", QMessageBox.Yes | QMessageBox.Yes)
            return

        if not os.path.exists('bak'):
            os.makedirs('bak')

        fileContent = open(filepath, 'r', encoding='utf-8').read()
        bak_name = 'bak/bak_' + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + filepath[-5:]
        with open(bak_name, 'w', encoding='utf-8') as f:
            f.write(fileContent)

        if filepath[-4:] == 'prsv':
            self.cryptor.en_text = fileContent
            de_rst = self.cryptor.decrypt()
            if de_rst == Cryptor.DATA:
                self.loadData()
            elif de_rst == Cryptor.SLOT:
                self.loadSlot()
            else:
                QMessageBox.critical(self, "错误", "解密失败", QMessageBox.Yes | QMessageBox.Yes)
        elif filepath[-4:] == 'json':
            dict = json.loads(fileContent)
            if 'starterData' in dict:
                self.cryptor.dict_data = dict
                self.loadData()
            elif 'party' in dict:
                self.cryptor.dict_slot = dict
                self.loadSlot()
            else:
                QMessageBox.critical(self, "错误", "JSON文件格式不正确", QMessageBox.Yes | QMessageBox.Yes)

    def loadData(self):
        for i in range(0, 9):
            self.LWidgetGen[i].clear()
            for pm in generations[i]:
                if pm in starters:
                    pix = QPixmap(png_dict[pm] + '.png')
                    caughtAttr = self.cryptor.dict_data['dexData'][str(pm)]['caughtAttr']
                    winCount = self.cryptor.dict_data['starterData'][str(pm)]['classicWinCount']
                    abilityAttr = self.cryptor.dict_data['starterData'][str(pm)]['abilityAttr']
                    passiveAttr = self.cryptor.dict_data['starterData'][str(pm)]['passiveAttr']
                    pListItem = QListWidgetItem(self.paintStarterIcon(pix, passiveAttr, bin(caughtAttr)[2:], winCount, abilityAttr), '')
                    pListItem.setData(Qt.UserRole, pm)
                    pListItem.setSizeHint(QSize(44, 40))
                    self.LWidgetGen[i].addItem(pListItem)

    def loadSlot(self):
        self.listWidget.clear()
        self.select_partner = {}

        for species in self.cryptor.dict_slot['party']:
            form = 's' if species['shiny'] else ''
            if species['formIndex'] != 0 and species['species'] in form_dict:
                form += f'-{form_dict[species["species"]][species["formIndex"]].lower()}'
            pix = QPixmap(png_dict[species['species']] + form + '.png')

            strShiny = '10010111' if species['shiny'] else '10010101'
            passiveAttr = 3 if species['passive'] else 0
            pListItem = QListWidgetItem(self.paintStarterIcon(pix, passiveAttr, strShiny, 0, 1), '')
            pListItem.setData(Qt.UserRole, species['id'])
            pListItem.setSizeHint(QSize(44, 40))
            self.listWidget.addItem(pListItem)

        self.spinBox_money.setValue(self.cryptor.dict_slot['money'])
        tmp = self.cryptor.dict_slot['pokeballCounts']
        self.spinBox_pb.setValue(tmp['0'])
        self.spinBox_gb.setValue(tmp['1'])
        self.spinBox_ub.setValue(tmp['2'])
        self.spinBox_rb.setValue(tmp['3'])
        self.spinBox_mb.setValue(tmp['4'])

        for item in self.cryptor.dict_slot['modifiers']:
            if item['typeId'] == 'EXP_SHARE':
                self.spinBox_es.setValue(item['stackCount'])
            elif item['typeId'] == 'EXP_BALANCE':
                self.spinBox_eb.setValue(item['stackCount'])
            elif item['typeId'] == 'EXP_CHARM':
                self.spinBox_ec.setValue(item['stackCount'])
            elif item['typeId'] == 'SUPER_EXP_CHARM':
                self.spinBox_sec.setValue(item['stackCount'])
            elif item['typeId'] == 'ABILITY_CHARM':
                self.spinBox_ac.setValue(item['stackCount'])
            elif item['typeId'] == 'SHINY_CHARM':
                self.spinBox_sc.setValue(item['stackCount'])
            elif item['typeId'] == 'HEALING_CHARM':
                self.spinBox_hc.setValue(item['stackCount'])
            elif item['typeId'] == 'GOLDEN_POKEBALL':
                self.spinBox_pb_golden.setValue(item['stackCount'])
            elif item['typeId'] == 'BERRY_POUCH':
                self.spinBox_bp.setValue(item['stackCount'])
            elif item['typeId'] == 'MEGA_BRACELET':
                self.checkBox_mega.setChecked(True)
            elif item['typeId'] == 'DYNAMAX_BAND':
                self.checkBox_gmax.setChecked(True)
            elif item['typeId'] == 'TERA_ORB':
                self.checkBox_tera.setChecked(True)

    @staticmethod
    def paintPixShiny(str_shiny: str):
        pix_shiny = QPixmap(":pokemon/pokemon/part/shiny.png")
        pix = QPixmap(QSize(pix_shiny.width() * str_shiny.count('1'), pix_shiny.height()))
        pix.fill(Qt.transparent)
        painter = QPainter(pix)
        colors = ['red', 'skyblue', 'yellow']
        shiny_number = 0
        for i in range(0, 3):
            if str_shiny[i] == '1':
                painter.drawPixmap(pix_shiny.width() * shiny_number, 0, MainWindow.paintPixColor(pix_shiny, colors[i]))
                shiny_number += 1
        painter.end()
        return pix

    @staticmethod
    def paintPixColor(pix: QPixmap, color):
        painter = QPainter(pix)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pix.rect(), QColor(color))
        painter.end()
        return pix

    @staticmethod
    def paintPixOpacity(pixmap: QPixmap):
        tmpPix = QPixmap(pixmap.size())
        tmpPix.fill(Qt.transparent)
        painter = QPainter(tmpPix)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)
        painter.fillRect(tmpPix.rect(), QColor(0, 0, 0, 100))  # 根据QColor中第四个参数设置透明度，0～255
        painter.end()
        return tmpPix

    @staticmethod
    def paintStarterIcon(pixmap: QPixmap, passiveAttr: int, caughtAttr: str, winCount: int, abilityAttr: int):
        emptyPix = QPixmap(40, 40)
        emptyPix.fill(Qt.transparent)

        painter = QPainter(emptyPix)

        if passiveAttr == 3:
            painter.drawPixmap(0, 0, QPixmap(':pokemon/pokemon/part/passive_bg.png').scaled(38, 38, Qt.KeepAspectRatioByExpanding))

        if len(caughtAttr) < 8:
            MainWindow.paintPixColor(pixmap, 'black')
            painter.drawPixmap(0, 5, pixmap)
        else:
            painter.drawPixmap(0, 5, pixmap)
            if caughtAttr[-2:] == '11':
                pixmap_shiny = MainWindow.paintPixShiny(caughtAttr[-7:-4])
                painter.drawPixmap(40 - pixmap_shiny.width(), 0, pixmap_shiny)
            if winCount > 0:
                pixmap_champion = QPixmap(':pokemon/pokemon/part/champion.png')
                painter.drawPixmap(0, 30, pixmap_champion)
            if abilityAttr >= 4:
                transform = QTransform()
                transform.rotate(-45)
                pixmap_ability = QPixmap(':pokemon/pokemon/part/ability_capsule.png').scaled(13, 13, Qt.KeepAspectRatioByExpanding).transformed(transform)
                painter.drawPixmap(26, 5, pixmap_ability)
        painter.end()
        return QIcon(emptyPix)

    @pyqtSlot()
    def slot_switch(self):
        sender = self.sender()
        if isinstance(sender, QPushButton):
            self.stackedWidget.setCurrentIndex(int(sender.text()) - 1)

    @pyqtSlot()
    def on_pushButton_select_clicked(self):
        for LWidget in self.LWidgetGen:
            for row in range(LWidget.count()):
                LWidget.item(row).setSelected(True)

    @pyqtSlot()
    def on_pushButton_select_none_clicked(self):
        for LWidget in self.LWidgetGen:
            for row in range(LWidget.count()):
                LWidget.item(row).setSelected(False)

    @pyqtSlot()
    def on_pushButton_select_passed_clicked(self):
        for LWidget in self.LWidgetGen:
            for row in range(LWidget.count()):
                number = LWidget.item(row).data(Qt.UserRole)
                LWidget.item(row).setSelected(False)
                if self.cryptor.dict_data['starterData'][str(number)]['classicWinCount'] > 0:
                    LWidget.item(row).setSelected(True)

    @pyqtSlot()
    def on_pushButton_select_have_clicked(self):
        for LWidget in self.LWidgetGen:
            for row in range(LWidget.count()):
                number = LWidget.item(row).data(Qt.UserRole)
                LWidget.item(row).setSelected(False)
                if self.cryptor.dict_data['dexData'][str(number)]['caughtAttr'] > 0:
                    LWidget.item(row).setSelected(True)

    @pyqtSlot(QListWidgetItem, QListWidgetItem)
    def on_listWidget_currentItemChanged(self, current, previous):
        if current is None:
            return

        for species in self.cryptor.dict_slot['party']:
            if species['id'] == current.data(Qt.UserRole):
                self.select_partner = species
                self.spinBox_lv.setValue(species['level'])
                self.spinBox_hp.setRange(0, species['stats'][0])
                self.spinBox_hp.setValue(species['hp'])
                self.spinBox_friendship.setValue(species['friendship'])
                self.comboBox_luck.setCurrentText(str(species['luck']))
                self.comboBox_fusionLuck.setCurrentText(str(species['fusionLuck']))
                self.comboBox_ability.setCurrentIndex(species['abilityIndex'])
                self.checkBox_rus.setChecked(species['pokerus'])
                ui_stats = [self.spinBox_stat_1, self.spinBox_stat_2, self.spinBox_stat_3, self.spinBox_stat_4, self.spinBox_stat_5, self.spinBox_stat_6]
                ui_ivs = [self.spinBox_iv_1, self.spinBox_iv_2, self.spinBox_iv_3, self.spinBox_iv_4, self.spinBox_iv_5, self.spinBox_iv_6]
                ui_moves = [self.comboBox_move_1, self.comboBox_move_2, self.comboBox_move_3, self.comboBox_move_4]
                ui_ppUsed = [self.spinBox_used_1, self.spinBox_used_2, self.spinBox_used_3, self.spinBox_used_4]
                ui_ppUp = [self.spinBox_up_1, self.spinBox_up_2, self.spinBox_up_3, self.spinBox_up_4]
                for i in range(6):
                    ui_stats[i].setValue(species['stats'][i])
                    ui_ivs[i].setValue(species['ivs'][i])
                    if i < 4:
                        ui_moves[i].setCurrentText(move_dict[species['moveset'][i]['moveId']])
                        ui_ppUsed[i].setValue(species['moveset'][i]['ppUsed'])
                        ui_ppUp[i].setValue(species['moveset'][i]['ppUp'])
                break

    @pyqtSlot()
    def on_action_file_triggered(self):
        filepath, fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "All Type(*.*);;Prsv Files(*.prsv);;Json Files(*.json)")
        self.readFile(filepath)

    @pyqtSlot()
    def on_pushButton_prsv_data_clicked(self):
        if self.cryptor.encrypt(Cryptor.DATA):
            filepath = '/data_' + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + '.prsv'
            filePath = QFileDialog.getSaveFileName(self, "保存", os.getcwd() + filepath, "Prsv Files(*.prsv)")
            if filePath[0] == '': return
            with open(filePath[0], 'w', encoding='utf-8') as f:
                f.write(self.cryptor.en_text)
            QMessageBox.information(self, "成功", "保存成功")

    @pyqtSlot()
    def on_pushButton_prsv_slot_clicked(self):
        if self.cryptor.encrypt(Cryptor.SLOT):
            filename = '/result_' + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + '.prsv'
            filePath = QFileDialog.getSaveFileName(self, "保存", os.getcwd() + filename, "Prsv Files(*.prsv)")
            if filePath[0] == '': return
            with open(filePath[0], 'w', encoding='utf-8') as f:
                f.write(self.cryptor.en_text)
            QMessageBox.information(self, "成功", "保存成功")

    @pyqtSlot()
    def on_pushButton_json_data_clicked(self):
        filename = '/data_' + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + '.json'
        filePath = QFileDialog.getSaveFileName(self, "保存", os.getcwd() + filename, "Json Files(*.json)")
        if filePath[0] == '': return
        with open(filePath[0], 'w', encoding='utf-8') as f:
            json.dump(self.cryptor.dict_data, f, ensure_ascii=False, indent=4)
        QMessageBox.information(self, "成功", "保存成功")

    @pyqtSlot()
    def on_pushButton_slot_json_clicked(self):
        filename = '/slot_' + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + '.json'
        filePath = QFileDialog.getSaveFileName(self, "保存", os.getcwd() + filename, "Json Files(*.json)")
        if filePath[0] == '': return
        with open(filePath[0], 'w', encoding='utf-8') as f:
            json.dump(self.cryptor.dict_slot, f, ensure_ascii=False, indent=4)
        QMessageBox.information(self, "成功", "保存成功")

    @pyqtSlot()
    def on_pushButton_confire_slot_partner_clicked(self):
        if self.select_partner == {}:
            return

        self.select_partner['nature'] = self.comboBox_nature.currentIndex()
        self.select_partner['level'] = self.spinBox_lv.value()
        self.select_partner['hp'] = self.spinBox_hp.value()
        self.select_partner['friendship'] = self.spinBox_friendship.value()
        self.select_partner['luck'] = int(self.comboBox_luck.currentText())
        self.select_partner['fusionLuck'] = int(self.comboBox_fusionLuck.currentText())
        self.select_partner['abilityIndex'] = self.comboBox_ability.currentIndex()
        self.select_partner['pokerus'] = self.checkBox_rus.isChecked()

        ui_stats = [self.spinBox_stat_1, self.spinBox_stat_2, self.spinBox_stat_3, self.spinBox_stat_4, self.spinBox_stat_5, self.spinBox_stat_6]
        ui_ivs = [self.spinBox_iv_1, self.spinBox_iv_2, self.spinBox_iv_3, self.spinBox_iv_4, self.spinBox_iv_5, self.spinBox_iv_6]
        ui_moves = [self.comboBox_move_1, self.comboBox_move_2, self.comboBox_move_3, self.comboBox_move_4]
        ui_ppUsed = [self.spinBox_used_1, self.spinBox_used_2, self.spinBox_used_3, self.spinBox_used_4]
        ui_ppUp = [self.spinBox_up_1, self.spinBox_up_2, self.spinBox_up_3, self.spinBox_up_4]
        reversedMove = {v: k for k, v in move_dict.items()}
        for row in range(6):
            self.select_partner['stats'][row] = ui_stats[row].value()
            self.select_partner['ivs'][row] = ui_ivs[row].value()
            if row < 4:
                self.select_partner['moveset'][row]['moveId'] = reversedMove[ui_moves[row].currentText()]
                self.select_partner['moveset'][row]['ppUsed'] = ui_ppUsed[row].value()
                self.select_partner['moveset'][row]['ppUp'] = ui_ppUp[row].value()

    @pyqtSlot()
    def on_pushButton_confire_slot_player_clicked(self):
        if not self.cryptor.dict_slot:
            return

        self.cryptor.dict_slot['money'] = self.spinBox_money.value()
        self.cryptor.dict_slot['arena']['biome'] = self.comboBox_biome.currentData()
        self.cryptor.dict_slot['pokeballCounts'] = [self.spinBox_pb.value(), self.spinBox_gb.value(), self.spinBox_ub.value(), self.spinBox_rb.value(), self.spinBox_mb.value()]

        countDict, indexDict = {}, {}
        for index, item in enumerate(self.cryptor.dict_slot['modifiers']):
            countDict[item['typeId']] = item['stackCount']
            indexDict[item['typeId']] = index

        countDict['MEGA_BRACELET'] = 1 if self.checkBox_mega.isChecked() else 0
        countDict['DYNAMAX_BAND'] = 1 if self.checkBox_gmax.isChecked() else 0
        countDict['TERA_ORB'] = 1 if self.checkBox_tera.isChecked() else 0
        countDict['GOLDEN_POKEBALL'] = self.spinBox_pb_golden.value()
        countDict['EXP_SHARE'] = self.spinBox_es.value()
        countDict['EXP_BALANCE'] = self.spinBox_eb.value()
        countDict['EXP_CHARM'] = self.spinBox_ec.value()
        countDict['SUPER_EXP_CHARM'] = self.spinBox_sec.value()
        countDict['GOLDEN_EXP_CHARM'] = self.spinBox_gec.value()
        countDict['SHINY_CHARM'] = self.spinBox_sc.value()
        countDict['HEALING_CHARM'] = self.spinBox_hc.value()

        for itemId, count in countDict.items():
            if itemId in indexDict:
                self.cryptor.dict_slot['modifiers'][indexDict[itemId]]['stackCount'] = count
            else:
                if count > 0:
                    self.cryptor.dict_slot['modifiers'].append(ModifierType[itemId].value.fh_toJSON())

        self.cryptor.dict_slot['modifiers'] = [item for item in self.cryptor.dict_slot['modifiers'] if item['stackCount'] != 0]

    @pyqtSlot()
    def on_pushButton_confirm_data_clicked(self):
        if not self.cryptor.dict_data:
            QMessageBox.information(self, "提示", "未加载数据")
            return

        targetList = []
        for LWidget in self.LWidgetGen:
            for row in range(LWidget.count()):
                if LWidget.item(row).isSelected():
                    targetList.append(str(LWidget.item(row).data(Qt.UserRole)))

        if not targetList:
            QMessageBox.information(self, "提示", "未选中要修改的初始宝可梦")
            return

        changed = []
        if self.checkBox_species.isChecked():
            changed.append('已解锁精灵')
            for str_number in targetList:
                if self.cryptor.dict_data['dexData'][str_number]['caughtAttr'] == 0:
                    self.cryptor.dict_data['dexData'][str_number]['seenAttr'] = int("10000101", 2)
                    self.cryptor.dict_data['dexData'][str_number]['caughtAttr'] = int("10000101", 2)
                    self.cryptor.dict_data['dexData'][str_number]['ivs'] = [10, 10, 10, 10, 10, 10]
                    self.cryptor.dict_data['starterData'][str_number]['abilityAttr'] = 1

        if self.checkBox_pass.isChecked():
            changed.append('通关精灵')
            if self.radioButton_pass.isChecked():
                for str_number in targetList:
                    if self.cryptor.dict_data['starterData'][str_number]['classicWinCount'] == 0:
                        self.cryptor.dict_data['starterData'][str_number]['classicWinCount'] = 1
            else:
                for str_number in targetList:
                    self.cryptor.dict_data['starterData'][str_number]['classicWinCount'] = 0

        if self.checkBox_sex.isChecked():
            changed.append('性别')
            for str_number in targetList:
                if self.cryptor.dict_data['dexData'][str_number]['caughtAttr'] == 0:
                    continue

                tmp = bin(self.cryptor.dict_data['dexData'][str_number]['caughtAttr'])[2:]
                if int(str_number) in sex_01:
                    self.cryptor.dict_data['dexData'][str_number]['caughtAttr'] = int(f'{tmp[:-4]}01{tmp[-2:]}', 2)
                elif int(str_number) in sex_10:
                    self.cryptor.dict_data['dexData'][str_number]['caughtAttr'] = int(f'{tmp[:-4]}10{tmp[-2:]}', 2)
                else:
                    self.cryptor.dict_data['dexData'][str_number]['caughtAttr'] = int(f'{tmp[:-4]}11{tmp[-2:]}', 2)

        if self.checkBox_iv.isChecked():
            changed.append('个体')
            if self.comboBox_iv.currentText() == "满个体":
                for str_number in targetList:
                    self.cryptor.dict_data['dexData'][str_number]['ivs'] = [31, 31, 31, 31, 31, 31]
            else:
                for str_number in targetList:
                    self.cryptor.dict_data['dexData'][str_number]['ivs'] = [randint(0, 31) for i in range(6)]

        if self.checkBox_ability.isChecked():
            changed.append('特性')
            ability_value = self.checkBox_ability_1.isChecked() * 1 + self.checkBox_ability_2.isChecked() * 2 + self.checkBox_ability_hide.isChecked() * 4
            if ability_value == 0:
                QMessageBox.critical(self, "错误", "特性不能修改为空")
                return
            for str_number in targetList:
                self.cryptor.dict_data['starterData'][str_number]['abilityAttr'] = ability_value

        if self.checkBox_nature.isChecked():
            changed.append('性格')
            natureAttr = sum([self.comboBox_starterNatures.itemData(index) for index in self.comboBox_starterNatures.checkedIndexes()])
            for str_number in targetList:
                self.cryptor.dict_data['dexData'][str_number]['natureAttr'] = natureAttr

        if self.checkBox_egg.isChecked():
            changed.append('蛋招式')
            egg_value = self.checkBox_egg_1.isChecked() * 1 + self.checkBox_egg_2.isChecked() * 2 + self.checkBox_egg_3.isChecked() * 4 + self.checkBox_egg_4.isChecked() * 8
            for str_number in targetList:
                self.cryptor.dict_data['starterData'][str_number]['eggMoves'] = egg_value

        if self.checkBox_passive.isChecked():
            changed.append('被动')
            passive_value = 3 if self.radioButton_passive.isChecked() else 0
            for str_number in targetList:
                self.cryptor.dict_data['starterData'][str_number]['passiveAttr'] = passive_value

        if self.checkBox_shine.isChecked():
            changed.append('闪光')
            shine_part = ''.join(["1" if self.checkBox_red.isChecked() else "0",
                                  "1" if self.checkBox_blue.isChecked() else "0",
                                  "1" if self.checkBox_yellow.isChecked() else "0"])
            for str_number in targetList:
                tmp = bin(self.cryptor.dict_data['dexData'][str_number]['caughtAttr'])[2:]
                if shine_part == '000':
                    self.cryptor.dict_data['dexData'][str_number]['caughtAttr'] = int(f'{tmp[:-7]}000{tmp[-4:-2]}01', 2)
                else:
                    self.cryptor.dict_data['dexData'][str_number]['caughtAttr'] = int(tmp[:-7] + shine_part + tmp[-4:-2] + '11', 2)

        if self.checkBox_candy.isChecked():
            for str_number in targetList:
                self.cryptor.dict_data['starterData'][str_number]['candyCount'] = self.spinBox_candy.value()

        if not changed:
            QMessageBox.information(self, "提示", f"未选中要修改的项目")
        else:
            self.loadData()
            QMessageBox.information(self, "成功", f"修改 {'、'.join(changed)} 成功")

    @pyqtSlot()
    def on_pushButton_random_clicked(self):
        import random
        for species in starters:
            str_number = str(species)
            if self.cryptor.dict_data['dexData'][str_number]['hatchedCount'] == 0:
                self.cryptor.dict_data['starterData'][str_number]['eggMoves'] = 0
            elif self.cryptor.dict_data['dexData'][str_number]['hatchedCount'] >= 4:
                self.cryptor.dict_data['starterData'][str_number]['eggMoves'] = 15
            elif self.cryptor.dict_data['dexData'][str_number]['hatchedCount'] == 3:
                rand = ['1110', '1101', '1011', '0111']
                self.cryptor.dict_data['starterData'][str_number]['eggMoves'] = int(rand[random.randint(0, len(rand) - 1)], 2)
            elif self.cryptor.dict_data['dexData'][str_number]['hatchedCount'] == 2:
                rand = ['0011', '1001', '1010', '0101', '0110', '1100']
                self.cryptor.dict_data['starterData'][str_number]['eggMoves'] = int(rand[random.randint(0, len(rand) - 1)], 2)
            elif self.cryptor.dict_data['dexData'][str_number]['hatchedCount'] == 1:
                rand = ['0001', '1000', '0010', '0100']
                self.cryptor.dict_data['starterData'][str_number]['eggMoves'] = int(rand[random.randint(0, len(rand) - 1)], 2)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if not urls:
            return

        self.readFile(urls[0].toLocalFile())
