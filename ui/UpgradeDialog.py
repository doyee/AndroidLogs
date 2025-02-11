# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpgradeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpgradeDialog(object):
    def setupUi(self, UpgradeDialog):
        UpgradeDialog.setObjectName("UpgradeDialog")
        UpgradeDialog.setWindowModality(QtCore.Qt.NonModal)
        UpgradeDialog.resize(400, 122)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UpgradeDialog.sizePolicy().hasHeightForWidth())
        UpgradeDialog.setSizePolicy(sizePolicy)
        UpgradeDialog.setMinimumSize(QtCore.QSize(400, 122))
        UpgradeDialog.setMaximumSize(QtCore.QSize(400, 122))
        self.gridLayout = QtWidgets.QGridLayout(UpgradeDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_ico_logger = QtWidgets.QLabel(UpgradeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ico_logger.sizePolicy().hasHeightForWidth())
        self.label_ico_logger.setSizePolicy(sizePolicy)
        self.label_ico_logger.setBaseSize(QtCore.QSize(0, 0))
        self.label_ico_logger.setPixmap(QtGui.QPixmap(":/lable_icon/resource/app_icon.svg"))
        self.label_ico_logger.setScaledContents(True)
        self.label_ico_logger.setObjectName("label_ico_logger")
        self.horizontalLayout_2.addWidget(self.label_ico_logger)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lable_curr_version = QtWidgets.QLabel(UpgradeDialog)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lable_curr_version.setFont(font)
        self.lable_curr_version.setTextFormat(QtCore.Qt.AutoText)
        self.lable_curr_version.setScaledContents(False)
        self.lable_curr_version.setObjectName("lable_curr_version")
        self.verticalLayout.addWidget(self.lable_curr_version)
        self.label_latest_version = QtWidgets.QLabel(UpgradeDialog)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        self.label_latest_version.setFont(font)
        self.label_latest_version.setObjectName("label_latest_version")
        self.verticalLayout.addWidget(self.label_latest_version)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_ignore = QtWidgets.QPushButton(UpgradeDialog)
        self.pushButton_ignore.setEnabled(True)
        self.pushButton_ignore.setObjectName("pushButton_ignore")
        self.horizontalLayout.addWidget(self.pushButton_ignore)
        self.pushButton_upgrade = QtWidgets.QPushButton(UpgradeDialog)
        self.pushButton_upgrade.setEnabled(True)
        self.pushButton_upgrade.setObjectName("pushButton_upgrade")
        self.horizontalLayout.addWidget(self.pushButton_upgrade)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(UpgradeDialog)
        self.pushButton_ignore.clicked.connect(UpgradeDialog.ignoreThisVersion)
        self.pushButton_upgrade.clicked.connect(UpgradeDialog.showDownload)
        QtCore.QMetaObject.connectSlotsByName(UpgradeDialog)

    def retranslateUi(self, UpgradeDialog):
        _translate = QtCore.QCoreApplication.translate
        UpgradeDialog.setWindowTitle(_translate("UpgradeDialog", "检查更新"))
        self.lable_curr_version.setAccessibleName(_translate("UpgradeDialog", "当前版本: "))
        self.lable_curr_version.setText(_translate("UpgradeDialog", "当前版本:"))
        self.label_latest_version.setAccessibleName(_translate("UpgradeDialog", "最新版本: "))
        self.label_latest_version.setText(_translate("UpgradeDialog", "最新版本:"))
        self.pushButton_ignore.setText(_translate("UpgradeDialog", "忽略"))
        self.pushButton_upgrade.setText(_translate("UpgradeDialog", "更新"))
import app_icons_rc
