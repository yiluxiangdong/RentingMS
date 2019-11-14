#!/usr/bin/python
#-*- coding:utf-8 _*-
import  pymysql
import json
import requests, random, datetime,time,re
from urllib import request
class getInfoDate:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        try:
            self.conn = pymysql.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            self.cour = self.conn.cursor()
        except Exception as  e:
            print ('数据库连接失败',e)
#生成最新的房源编号
    def get_housing_number(self,mobile):
        #获取原始的编号
        sql = "SELECT s.ext_code,s.value  FROM  rms_org_setting s LEFT JOIN  rms_landlord l ON l.id=s.landlord_id WHERE l.mobile={} ORDER BY RAND()" \
              " LIMIT 1".format(mobile)
        try:
            self.cour.execute(sql)
            info = self.cour.fetchone()
            housecode= info[0]
            prefix=json.loads(info[1])['prefix']
            noLength=json.loads(info[1])['noLength']
            code =[(str(int(housecode)+1).zfill(int(noLength))),str(prefix)+(str(int(housecode)+1).zfill(int(noLength)))]
        except Exception as e:
            code = '该运营商还没有设置房源编号'
        return code
        #['00003', 'SONGGUANG00003']
#创建房源
    def addhousing_detaill(self, mobiles,key,pro):
        result = ''
        orgset = self.get_housing_number(mobiles)
        #获取业主的缴费日期
        paydate = self.getPay(mobiles, key, 'landlordPayDayFlag', 'landlordPayDayList', 'landlordNeedPayDays')
        try:
            self.cour.callproc(pro, (mobiles, orgset[0], orgset[1], paydate[0], paydate[1], result))
            date = self.cour.fetchone()[0]
        except Exception as e:
            date = e
        print(date)
        return date
    def addHousing(self,mobiles,rentType):
        keys=[]
        if rentType == 1:
            keys = ['JOINGRENT_PAY_SET','pro_Add_joinhouse']
        elif rentType == 2:
            keys = ['FULLRENT_PAY_SET','pro_Add_Fullhouse']
        elif rentType == 3:
            keys = ['JZSRENT_PAY_SET','pro_Add_Centralizedhouse']
        result=self.addhousing_detaill(mobiles,keys[0] ,keys[1])
        return result
#新版创建房源g#
    def addhouse_v2(self,mobiles,houseType):
        #mobiles, extcode, extcodename, PayDayFlag, NeedPayDays, houseType, result
        #houseType1-合租2-整租3-集中式
        orgset = self.get_housing_number(mobiles)
        key = lambda x: 'JOINGRENT_PAY_SET' if houseType==1 else ('FULLRENT_PAY_SET' if houseType==2 else ('JZSRENT_PAY_SET' if houseType==3 else ""))
        # 获取业主的缴费日期
        paydate = self.getPay(mobiles, key(True), 'landlordPayDayFlag', 'landlordPayDayList', 'landlordNeedPayDays')
        result=''
        try:
            self.cour.callproc("pro_Add_house", (mobiles, orgset[0], orgset[1], paydate[0], paydate[1],houseType, result))
            date = self.cour.fetchone()[0]
        except Exception as e:
            date = e
        print(date)
        return date
#以上为创建集中房源#
# 获取运营商设置的付款时间
    def getPay(self, mobile, key, Flag, PayDaysList, PayDays):
        sql = "select value from rms_landlord_setting s  LEFT JOIN rms_landlord l ON s.landlord_id=l.id WHERE l.mobile={} and s.`key`='{}' ".format(
            mobile, key)
        self.cour.execute(sql)
        date = json.loads(self.cour.fetchone()[0])
        PayDayFlag = date[Flag]
        if PayDayFlag == 1:
            for date in date[PayDaysList]:
                if date['startDay'] <= int(datetime.date.today().strftime('%d')) and date['endDay'] >= int(
                        datetime.date.today().strftime('%d')):
                    needPayDays = (date['needPayDays'])
                    result = [PayDayFlag, needPayDays]
                    return result
        else:
            result = [PayDayFlag, date[PayDays]]
            return result
#以上为获取缴费时间#
#签约confirmbyrenter 1-不需要租客确认签约2-需要租客确认签约
    def sign_contract(self, mobiles,rentType,needconfirm,isFixedrenter=1):
        #rentType 1-合租 2-整租 3-集中式
        #isFixedrenter 1-固定 非1-随机租客
        #confirmbyrenter 1-不需要租客确认签约2-需要租客确认签约3-需要租客确认签约并生成合同
        result = ''
        key = lambda x: 'JOINGRENT_PAY_SET' if rentType == 1 else ('FULLRENT_PAY_SET' if rentType == 2 else ('JZSRENT_PAY_SET' if rentType == 3 else ""))
        paydate = self.getPay(mobiles, key(True),'renterPayDayFlag', 'renterPayDayList', 'renterNeedPayDays')
        try:
            time.sleep(1)
            self.cour.callproc('proc_Sign_contract', (mobiles, rentType, paydate[0], paydate[1],isFixedrenter,needconfirm,result))
            date = self.cour.fetchone()[0]
        except Exception as e:
            date = e
        print(date)
        return date
#以上为租客签约#
# 获取运营商ID
    def getLandlordid(self, mobile):
        # 获取原始的编号
        sql = "SELECT id   FROM  rms_landlord  WHERE  mobile={}".format(mobile)
        try:
            self.cour.execute(sql)
            info = self.cour.fetchone()[0]
        except Exception as e:
            info = '该运营商不存在'
        return info

        # 获取运营商是否存在该小区
    def get_estate_account(self, landlordid,areaname):
        sql = "SELECT COUNT(1)  FROM  rms_area WHERE landlord_id={} AND  area_name  like '%{}%'".format(landlordid,areaname)
        try:
            self.cour.execute(sql)
            info = self.cour.fetchone()[0]
        except Exception as e:
            info = ''
        return info
# 获取小区信息
    def get_estate_info(self):
        url = "http://api.map.baidu.com/place/v2/search"
        distrctlist=["罗湖","福田","南山","盐田","龙岗","宝安","光明","坪山","大鹏","龙华"]
        distrct=random.choice(distrctlist)
        querystring={"query":"小区","region":distrct,"output":"json","ak":"b3Ix8q6DPj72LtZyHVrpfXKulw1eip7Z"}
        response = requests.request("GET", url, params=querystring)
        r = response.json()
        date=random.choice(r['results'])
        return date
    def add_estate(self,mobile,areatype=1):
        date=self.get_estate_info()
        f = lambda areatype:'集中式小区' if areatype!=1 else'分散式小区'
        if len(date)==9:
            # 判断是否在该运营商已经存在
            Landlordid = self.getLandlordid(mobile)
            name = str(date['name'])
            result = self.get_estate_account(Landlordid, name)
            if result == 0:
                try:
                    sql="insert into rms_area(area_name,landlord_id,create_time,create_user_id,longitude,latitude,address,area_type,province,city,district)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,Landlordid,datetime.datetime.now(),self.getuserid(mobile),str(date['location']['lng']),str(date['location']['lat']),str(date['address']),areatype,str(date['province']),str(date['city']),str(date['area']))
                    self.cour.execute(sql)
                    self.conn.commit()
                    info= ('{},{}创建成功'.format(f(areatype),str(date['name'])))
                except Exception as  e:
                    print(e)
                    self.conn.rollback()
                    info=('sql执行失败{}创建失败'.format(f(areatype)))
                    return info
            else:
                info=('该运营商已经存在{}创建失败'.format(str(date['name'])))
        else:
                info=('数据返回异常{}创建失败'.format(f(areatype)))
        return info
#以上为创建小区#
    def getuserid(self, mobile):
        # 获取原始的编号
        sql = "SELECT id  FROM  rms_user WHERE mobile={}".format(mobile)
        try:
            self.cour.execute(sql)
            info = self.cour.fetchone()[0]
        except Exception as e:
            info = '该用户不存在'
        return info
# 获取适合微信回调的流水
    def getnewflow(self, mobile,rentType):
        #rentType 1合租2整租3集中式
        sql="SELECT r.kft_order_no,r.money,h.name,c.bill_id,rr.name,rr.mobile FROM  rms_cash_flow r LEFT JOIN rms_cf_b c ON r.id=c.cashflow_id " \
            "LEFT JOIN rms_housing h ON c.housingId=h.id LEFT JOIN rms_renter rr ON c.renterId=rr.id  WHERE  r.pay_type='wxpay' and r.status!=1 and r.landlord_id={} " \
            "AND h.house_type=IF({}=3,2,1) AND if(h.house_type=2,1=1,h.rent_out_type={}) ORDER BY r.id DESC  LIMIT 1".format(self.getLandlordid(mobile),rentType,rentType)
        try:
            self.cour.execute(sql)
            info = self.cour.fetchone()
        except Exception as e:
            info = '该运营商还没有产生流水账单'
        return info
        # ['00003', 'SONGGUANG00003']
#委托上架#
    def getNO(self,tableName,fieldName,prefix):
        try:
            self.cour.callproc("proc_get_no", (tableName,fieldName,prefix))
            date = self.cour.fetchone()[0]
        except Exception as e:
            date = e
        return  date
    def  get_communityid(self):
        sql = "SELECT comm_no  FROM  t_housing_publish_community ORDER BY id DESC LIMIT 1"
        try:
            self.cour.execute(sql)
            info = self.cour.fetchone()[0]
        except Exception as e:
            info = '无法获取该字段'
        return info
    def  outhouseno(self):
        sql = "SELECT out_house_id  FROM  t_housing_publish_extend ORDER BY id DESC LIMIT 1"
        try:
            self.cour.execute(sql)
            info = self.cour.fetchone()[0]
        except Exception as e:
            info = '无法获取该字段'
        return info
    def authorize_release_houseinfo(self,mobiles):
        result=''
        comNO = self.get_communityid()
        houseNO = self.outhouseno()
        communityidno=comNO[0:13] + str(int(comNO[13:]) + 1).zfill(4)
        outhouseno=houseNO[0:13] + str(int(houseNO[13:]) + 1).zfill(4)
        try:
            self.cour.callproc("pro_authorize_release_houseinfo", (mobiles,communityidno,outhouseno,result))
        except Exception as e:
            print(e)
            self.cour.callproc("pro_complement_house_information", (re.findall('\d+', str(e))[1], result))
        date = self.cour.fetchone()[0]
        return  date
#账单支付/调起微信支付#
    def wx_paybill(self,mobiles,rentType,paytype):
        result=''
        try:
            self.cour.callproc("pro_wxpay", (mobiles, rentType,paytype,result))
        except Exception as e:
            print(e)
        date = self.cour.fetchone()[0]
        print(date)
        return date
#微信回调#
    def paybill_callback(self,mobile,dbip,type):
        date = self.getnewflow(mobile,type)
        renttype = lambda x: '合租' if type ==1 else ('整租' if type == 2 else ('集中式' if type == 3 else ""))
        url = 'http://{}/renting/app/WXNotifyTest/{}/{}/{}'.format(dbip,date[0], date[1]*100, 0)
        try:
            req = request.Request(url)
            page = request.urlopen(req).read()
            status = json.loads(str(page.decode('utf-8')))['msg']
            payresult = lambda t: '成功' if 'SUCCESS' in status else '重复,返回失败'
            resultinfo = '回调{},租客{}{},房源类型{},房源为{},账单共{}元,账单ID:{},流水ID:{}'.format(payresult(True),date[4], date[5],renttype(True),date[2], date[1], date[3], date[0])
        except Exception as e:
            resultinfo=e
        print(resultinfo)
        return resultinfo


    def __del__(self):
        self.cour.close()
        self.conn.close()

if __name__ == '__main__':
    renttest = getInfoDate('10.18.136.225','root','111111','renting_test2')
    date=renttest.getnewflow('18165706145',3)
    print(date)