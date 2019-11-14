#!/usr/bin/python
# -*- coding:  utf-8 -*-
# 打包命令pyinstaller -F -c -w -i static/img.ico setup.py
# 打包命令pyinstaller -F -c -w -i static/img.ico bin/run.py
import sys
import PyQt5
from PyQt5.QtWidgets import QMessageBox
from main.main import getInfoDate
from PyQt5.QtGui import QIcon
from  main.mainpage import Ui_Dialog
import logging

class MyAPP(PyQt5.QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MyAPP, self).__init__()
        self.setupUi(self)
        self.initUI()
        self.info = None
        self.setWindowIcon(QIcon('static/img.ico'))
        self.setWindowTitle('测试工具')
        self.setFixedSize(370,200)
        self.lineEdit.setText('18165706145')
        self.hz.setChecked(True)
        self.fixrenter.setChecked(True)
        with open('static/window.qss', 'r') as q:
            self.setStyleSheet(q.read())

    def initUI(self):
        #切换数据库
        self.dburl.currentTextChanged.connect(self.getlandermoile_v2)
        #微信预回调
        self.precallbackbt.clicked.connect(lambda :self.wxpaybill(1))
        #微信回调
        self.wxpush.clicked.connect(self.wx_callback)
        #添加房源
        self.addhouse.clicked.connect(self.add_house)
        # 添加小区
        self.pushButton.clicked.connect(self.add_estate)
        #委托上架房源
        self.pushhouse.clicked.connect(self.house_entrust)
        # 不需要租客确认签约1
        self.pbcommit.clicked.connect(lambda :self.renter_sign_contracts(1))
        # 需要租客确认签约生成待签约2
        self.signcontract.clicked.connect(lambda :self.renter_sign_contracts(2))
        # 需要租客确认签约生成合同3
        self.comsign.clicked.connect(lambda :self.renter_sign_contracts(3))
        #微信支付
        self.wxpaybt.clicked.connect(lambda :self.wxpaybill(2))

        # 获取常用运营商电话
    def getlandermoile_v2(self):
        ipdict = {'10.18.136.225':'18165706145', '10.18.136.226':'13560006000', '10.18.136.227':'13662299804'}
        self.lineEdit.setText(ipdict[self.dburl.currentText()])
#写日志
    def run_logs(self,info):
        logging.basicConfig(level=logging.DEBUG,
                            filename='logs/RentingMS.log',
                            filemode='a',
                            format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        logging.FileHandler('logs/RentingMS.log',encoding='utf-8')
        logging.info(info)
#获取常用运营商电话
    def getlandermoile(self):
        dbip=self.dburl.currentText()
        house_type = lambda x: '18165706145' if dbip=='10.18.136.225' else ('13560006000' if dbip=='10.18.136.226' else ('13662299804' if dbip == '10.18.136.227' else ""))
        self.lineEdit.setText(house_type(True))
#获取租房方式
    def rentertype(self):
        type = lambda x: 1 if self.hz.isChecked() else (2 if self.zz.isChecked() else (3 if self.jz.isChecked() else ""))
        return type(True)
#链接数据库
    def  connectdb(self):
        ip=self.dburl.currentText()
        renttest = getInfoDate(ip, 'root', '111111', 'renting_test2')
        return  renttest
#展示弹框信息
    def  showinfo(self,info):
        self.run_logs(info)
        QMessageBox.information(self, "提示", info, QMessageBox.Yes | QMessageBox.No)
#微信回调
    def wx_callback(self):
        mobile = self.lineEdit.text()
        type=self.rentertype()
        try:
            result = self.connectdb().paybill_callback(mobile,self.dburl.currentText(),type)
        except Exception as result:
            print(result)
        self.showinfo(result)
 #委托上架房源
    def house_entrust(self):
        mobile = self.lineEdit.text()
        result = self.connectdb().authorize_release_houseinfo(mobile)
        self.showinfo(result)
# 添加小区
    def add_estate(self):
        try:
            mobile = self.lineEdit.text()
            estate_type = lambda x: 2 if self.jz.isChecked() else 1
            result = self.connectdb().add_estate(mobile, estate_type(True))
            self.showinfo(result)
        except Exception as e:
            print(e)
# 添加房源
    def add_house(self):
        try:
            mobile = self.lineEdit.text()
            # result = self.connectdb().addHousing(mobile, house_type(True))
            result = self.connectdb().addhouse_v2(mobile, self.rentertype())
            self.showinfo(result)
        except Exception as e:
            print(e)
#签约
    def renter_sign_contracts(self,signType):
        #needrenter 1-不需要租客确认签约 # 2-需要租客确认签约生成待签约 3-需要租客确认签约生成合同
        try:
            mobile = self.lineEdit.text()
            fixrent = lambda x: 1 if self.fixrenter.isChecked() else 0
            result = self.connectdb().sign_contract(mobile, self.rentertype(), signType, fixrent(True))
            self.showinfo(result)
        except Exception as e:
            print(e)
#######################签约#################################################
#微信支付
    def wxpaybill(self,type):
        mobile = self.lineEdit.text()
        result = self.connectdb().wx_paybill(mobile,self.rentertype(),type)
        self.showinfo(result)



if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = MyAPP()
    window.show()
    sys.exit(app.exec_())
