# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 201)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 180, 362, 16))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignRight)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 166, 361, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 0, 251, 169))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.fixrenter = QtWidgets.QCheckBox(self.layoutWidget)
        self.fixrenter.setObjectName("fixrenter")
        self.horizontalLayout_2.addWidget(self.fixrenter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.dburl = QtWidgets.QComboBox(self.layoutWidget)
        self.dburl.setMaximumSize(QtCore.QSize(117, 16777215))
        self.dburl.setObjectName("dburl")
        self.dburl.addItem("")
        self.dburl.addItem("")
        self.dburl.addItem("")
        self.horizontalLayout_3.addWidget(self.dburl)
        spacerItem = QtWidgets.QSpacerItem(138, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.hz = QtWidgets.QRadioButton(self.layoutWidget)
        self.hz.setObjectName("hz")
        self.horizontalLayout_4.addWidget(self.hz, 0, QtCore.Qt.AlignHCenter)
        self.zz = QtWidgets.QRadioButton(self.layoutWidget)
        self.zz.setObjectName("zz")
        self.horizontalLayout_4.addWidget(self.zz, 0, QtCore.Qt.AlignHCenter)
        self.jz = QtWidgets.QRadioButton(self.layoutWidget)
        self.jz.setObjectName("jz")
        self.horizontalLayout_4.addWidget(self.jz, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.addhouse = QtWidgets.QPushButton(self.layoutWidget)
        self.addhouse.setObjectName("addhouse")
        self.horizontalLayout_5.addWidget(self.addhouse)
        self.pushhouse = QtWidgets.QPushButton(self.layoutWidget)
        self.pushhouse.setObjectName("pushhouse")
        self.horizontalLayout_5.addWidget(self.pushhouse)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pbcommit = QtWidgets.QPushButton(self.layoutWidget)
        self.pbcommit.setObjectName("pbcommit")
        self.horizontalLayout_6.addWidget(self.pbcommit)
        self.signcontract = QtWidgets.QPushButton(self.layoutWidget)
        self.signcontract.setObjectName("signcontract")
        self.horizontalLayout_6.addWidget(self.signcontract)
        self.comsign = QtWidgets.QPushButton(self.layoutWidget)
        self.comsign.setObjectName("comsign")
        self.horizontalLayout_6.addWidget(self.comsign)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.precallbackbt = QtWidgets.QPushButton(self.layoutWidget)
        self.precallbackbt.setObjectName("precallbackbt")
        self.horizontalLayout_7.addWidget(self.precallbackbt)
        self.wxpush = QtWidgets.QPushButton(self.layoutWidget)
        self.wxpush.setObjectName("wxpush")
        self.horizontalLayout_7.addWidget(self.wxpush)
        self.wxpaybt = QtWidgets.QPushButton(self.layoutWidget)
        self.wxpaybt.setObjectName("wxpaybt")
        self.horizontalLayout_7.addWidget(self.wxpaybt)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Copyright © 2019 Kilo-Coin All Rights Reserved"))
        self.label_3.setText(_translate("Dialog", "Version 1.0.1"))
        self.label.setText(_translate("Dialog", "运营商电话："))
        self.fixrenter.setText(_translate("Dialog", "固定租客"))
        self.label_5.setText(_translate("Dialog", "数据库地址："))
        self.dburl.setItemText(0, _translate("Dialog", "10.18.136.225"))
        self.dburl.setItemText(1, _translate("Dialog", "10.18.136.226"))
        self.dburl.setItemText(2, _translate("Dialog", "10.18.136.227"))
        self.hz.setText(_translate("Dialog", "合租"))
        self.zz.setText(_translate("Dialog", "整租"))
        self.jz.setText(_translate("Dialog", "集中"))
        self.pushButton.setText(_translate("Dialog", "创建小区"))
        self.addhouse.setText(_translate("Dialog", "创建房源"))
        self.pushhouse.setText(_translate("Dialog", "委托上架"))
        self.pbcommit.setText(_translate("Dialog", "签约"))
        self.signcontract.setText(_translate("Dialog", "待签约"))
        self.comsign.setText(_translate("Dialog", "确认签约"))
        self.precallbackbt.setText(_translate("Dialog", "预回调流水"))
        self.wxpush.setText(_translate("Dialog", "微信回调"))
        self.wxpaybt.setText(_translate("Dialog", "微信支付"))

