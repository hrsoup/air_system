from database import DBMapper
from application import Bill

class Register_user:#控制器0的基类
    def air_on(self):#开启空调
    def air_off(self):#关闭空调
    def change_wind(self):#调节风速
    def change_tem(self):#调节温度


class Register_admin:#控制器1的基类
    def create_air_main(self):#创建空调主机实例
    def power_on(self):#初始化空调系统
    def init_air(self):#空调子机参数初始化
    def print_hotel(self):#查看酒店空调运行状态
    def print_room(self):#查看房间空调运行状态

class Register_cashier:#控制器2的基类
    def __init__(self, user_id, room_id):          #认为只需要从用户界面获取user_id,room_id即可定位到订单信息
        self.user_id = user_id
        self.room_id = room_id
        self.bill_id = user_id+"-"+room_id         #自定义一种bill_id的生成规则
        self.bill = Bill(bill_id=self.bill_id, room_id=self.room_id, b_time=0, e_time=0,cost_all=0)
        #这边b_time,e_time我理解是用户使用了空调才开始计费，所以在创建订单对象时默认非空即可，当用户开关空调时再对b_time,e_time进行更新操作

    def create_bill(self):#创建账单详单
        self.bill.insert_data(self.bill_id)

    def print_bill(self):#查看账单详单
        record = self.bill.check_bill_item(self.bill_id)
        return record

    def get_begin(self):#获取用户入住时间——直接从User_item表中查
        sql_b = "select b_time from User_item where user_id="+self.user_id
        st = DBMapper.query(sql_b)
        if st.count() != 0:
            return st
        else:
            return -1                           #用户尚未入住的情况


    def get_end(self):#获取用户退房时间
        query_e ="select e_time from User_item where user_id="+self.user_id
        et = DBMapper.query(query_e)
        if et.count() != 0:
            return et
        else:
            return -1                            #用户尚未入住


class Register_manager:#控制器3的基类
    def create_form(self):#创建报表
    def print_form(self):#查看报表
