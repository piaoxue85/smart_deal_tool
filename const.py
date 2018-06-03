# coding=utf-8
class Const:
    class CError(Exception):
        pass

    class ConstError(CError):
        def __init__(self, expression, message):
            self.expression = expression
            self.message = message

    class ConstCaseError(CError):
        def __init__(self, expression, message):
            self.expression = expression
            self.message = message

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError(self.CError, "can't change const value!")
        if not name.isupper():
            raise self.ConstCaseError(self.CError, 'const "%s" is not all letters are capitalized' %name)
        self.__dict__[name] = value

import sys
sys.modules[__name__] = Const()

import const
##########login url##########
const.LOGIN_URL = "https://trade.cgws.com/cgi-bin/user/Login?function=tradeLogout"
const.ENTRUST_QUERY = "https://trade.cgws.com/cgi-bin/stock/EntrustQuery?function=MyAccount"
const.NEW_STOCK_URL = "http://newstock.cfi.cn/"
const.FUTU_HOST = "172.18.3.101"
const.FUTU_PORT = 11111
const.USER_FILE = "user.json"
const.SLEEP_TIME = 3
const.SHORT_SLEEP_TIME = 1
const.LONG_SLEEP_TIME = 10800 
const.SLEEP_INTERVAL = 30
const.CONCEPT_INPUT = "concepts/concept.csv"
##########stock type##########
const.MARKET_ALL = "MARKET_ALL"
const.SZZS = "sh"
const.SZ50 = "sz50"
const.HS300 = "hs300"
const.SZCZ = "sz"
const.CYBZ = "cyb"
const.ZZ500 = "zz500"
const.SUB_NEW_STOCK = "SUB_NEW_STOCK" 
const.MARKET_ELSE = "MARKET_ELSE"
const.INDEX_INFO = {const.SZZS: "000001",
                    const.SZ50: "000016",
                    const.HS300: "000300",
                    const.SZCZ: "399001",
                    const.CYBZ: "399006",
                    const.ZZ500: "000905"}
##########order type##########
const.SUBMITTED = 0
const.ONGOING = 1
##############################
const.DB_INFO = {'user':'root',  
                 'password':'123456', 
                 'host':'localhost',  
                 'database':'stock'}
const.UTF8 = "utf8"
const.SQL = "select * from %s"
const.RETRY_TIMES = 3
const.START_DATE = '2014-01-01'
const.AVERAGE_INDEX_LIST = ["700001_ALL", "700002_SH", "700003_SZ", "700004_CYB", "700005_SZ50", "700006_ZZ500", "700007_HS300", "700008_MSCI"]
const.C_INDEX = 1
const.C_CONCEPT = 2
const.C_STOCK = 3
const.C_COMBINATION = 4
const.C_AVERAGE = 5
##############################
# 150906130资金不足
# 150906135股数不够
# 长城的出错都是这个鸟样 alert("-990297020[-990297020]，出错了就反馈空的订单号，看看是不是自己定义一些exception来搞
const.NOT_ENOUGH_MONEY = 1
const.NOT_ENOUGH_STOCK = 2
const.SETTLEMENT_TIME = 3 #999003088
const.NOT_DEAL_TIME =4 #990297020
const.NOT_RIGHT_ORDER_ID = 5 #990268040订单号不对
const.LOGIN_FAIL = 100 #login fail
const.OTHER_ERROR = 999
#############################
const.HALTED_TABLE = "halted"
const.STOCK_INFO_TABLE = "stock"
const.CALENDAR_TABLE = "calendar"
const.DAILY_STATIC_TABLE = "static"
const.COMBINATION_INFO_TABLE = "combination"
const.DELISTED_INFO_TABLE = "delisted"
#############################
const.QUEUE_SZIE = 299
#############################
const.CLOSE = 0
const.REOPEN = 1
#############################
const.APPEND = 'append'
const.REPLACE = 'replace'
