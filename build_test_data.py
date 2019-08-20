# -*- coding: utf-8 -*-

import random,time, sys, datetime
import datetime,random
import string
from data import *

a= time.time()
print("开始构建")
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# def randomtimes(start, end, frmt="%Y-%m-%d %H:%M:%S"):
frmt="%Y-%m-%d %H:%M:%S"
start="2019-12-08 23:59:59"
end="2020-02-08 23:59:59"
stime = datetime.datetime.strptime(start, frmt)
etime = datetime.datetime.strptime(end, frmt)

#####################################################################

#平台停车场唯一标识
parking_lot_no=None

#商户号
merchant_no="etcp"


#停车时长
parking_time=None
#车牌类别（0：蓝牌，1：黄牌，2：白牌，3：黑色 4：绿牌，5：其他）
plate_color="0"
#停车状态(1：已进场,2：支付未离场，3：已离场，4：重复入场删除)
parking_status=None

##停车类别(0：临时，1：长租 2：免费  3：共享)
parking_type=""
#开票状态 0:未开票，1：开票中，2：开票成功，3：开票失败
electronic_invoice_type=""
#进场时间
in_time=""
#出场时间
out_time="1970-01-01 00:00:00"
#进场道闸名称
in_brake_name="进场道闸名称"
#进场道闸ID
in_brake_id="10000555"
#出场道闸名称
out_brake_name="出场道闸名称"
#出场道闸ID
out_brake_id="10000566"
#停车总金额(分)
parking_total_amount="12"
#备注
remarks=""
#共享停车预约单号（服务商回传）
reserve_order_no=""
#Long类型创建时间
create_time_long=None
#创建时间
create_time=None
#更新时间
update_time=None
#状态（1：新增2：修改3：删除）
status=None
#app租户
tenant_id="-1"
#支付租户
pay_tenant_id="-1"
#####################################################################
if len(sys.argv) == 1:
    lines = 20000000
    datafilename = "build_sharding_data"
else:
    lines = int(sys.argv[1])
    datafilename = sys.argv[2]
f = open(datafilename, "w", encoding="utf-8")
for _ in range(lines):
    parking_lot_no_name = random.choice(parking_lot_no_name_default)
    parking_lot_no = parking_lot_no_name[0] #int(random.random() * 10000000000000) + 5878590501908161544530000002
    third_parking_record_no = random.choice(third_parking_record_no_default)
    # parking_record_no ="p_" + str(random.randint(5878590501908161544530000002, 9878590501908161544530000002))
    parking_record_no ="p_" + str(int(random.random() * 10000000000000) + 5878590501908161544530000002)
    parking_lot_name = parking_lot_no_name[1]
    # merchant_no = random.choice(merchant_no, p=[0.8, 0.1, 0.1, 0, 0, 0, 0, 0, 0])
    plate_number_and_reserve = random.choice(plate_number_default)
    reserve_order_no = plate_number_and_reserve[0]
    plate_number = plate_number_and_reserve[1]
    parking_time=""
    status_1_4 = random.randint(1, 4)
    parking_status = status_1_4
    electronic_invoice_type=status_1_4
    status = "1"
    parking_type = _%4

    time_temp_obj = (random.random() * (etime - stime) + stime)
    in_time = '{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(time_temp_obj.year,time_temp_obj.month ,time_temp_obj.day,time_temp_obj.hour,time_temp_obj.minute,time_temp_obj.second)
    # in_time=(random.random() * (etime - stime) + stime).strftime('%Y-%m-%d %H:%M:%S')
    # in_time_strptime = datetime.datetime.strptime(in_time, frmt) #中间格式

    # datatime_obj_format = int(in_time[:4]), int(in_time[5:7]), int(in_time[8:10]),int(in_time[11:13]),int(in_time[14:16]),int(in_time[17:19])
    in_time_strptime = datetime.datetime(int(in_time[:4]), int(in_time[5:7]), int(in_time[8:10]),int(in_time[11:13]),int(in_time[14:16]),int(in_time[17:19]))  #中间格式

    time_temp_obj = (random.random() * (etime - in_time_strptime) + in_time_strptime)
    out_time = '{}-{}-{} {}:{}:{}'.format(time_temp_obj.year,time_temp_obj.month ,time_temp_obj.day,time_temp_obj.hour,time_temp_obj.minute,time_temp_obj.second)

    # out_time=(random.random() * (etime - in_time_strptime) + in_time_strptime).strftime('%Y-%m-%d %H:%M:%S')
    create_time= in_time
    # create_time_tmp = int(time.mktime(time.strptime(create_time, "%Y-%m-%d %H:%M:%S"))) #时间字符串转秒时间戳
    # create_time_tmp = int(time.mktime(time(int(in_time[:4]), int(in_time[5:7]), int(in_time[8:10]),int(in_time[11:13]),int(in_time[14:16]),int(in_time[17:19])))) #时间字符串转秒时间戳
    create_time_long = int(time_temp_obj.timestamp() * 1000)#毫秒时间戳
    # create_time_long = str(create_time_tmp) + str(numpy.random.randint(100,999)) #毫秒时间戳
    update_time=out_time

    # testdata=("|".join([parking_lot_no,parking_lot_name
    testdata = "%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%d|%s|%s" % (
        parking_lot_no
        ,parking_lot_name
        ,parking_record_no
        ,third_parking_record_no
        ,merchant_no
        ,plate_number
        ,parking_time
        ,plate_color
        ,parking_status
        ,parking_type
        ,electronic_invoice_type
        ,in_time
        ,out_time
        ,in_brake_name
        ,in_brake_id
        ,out_brake_name
        ,out_brake_id
        ,parking_total_amount
        ,remarks
        ,reserve_order_no
        ,create_time_long
        ,create_time
        ,update_time
        ,status
        ,_ + 1
        ,tenant_id
        , pay_tenant_id
    )
    f.write(testdata + "\n")

    # if _ + 1 == lines:
    #     percent = 100.0
    #     print('当前核算进度 : %s [%d/%d]' % (str(percent) + '%', _ + 1, lines), end='\n')
    # else:
    #     percent = round(1.0 * _ / lines * 100, 2)
    #     print('当前核算进度 : %s [%d/%d]' % (str(percent) + '%', _ + 1, lines), end='\r')

print("构建结束")
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("耗时：" + str(time.time() - a))