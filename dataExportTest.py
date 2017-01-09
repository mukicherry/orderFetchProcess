# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import csv
from utils import traversalFiles
import orderDataParse


# 从文件中读取json数据(带有'u字符,稍后处理,凡是从orderData处 处理的数据都得经过json.dumps()来转成想要的中文编码或者不带u的)
with open('taobao-orders/taobao-2016-orders-01.json', 'r') as file:
  orderData = json.load(file)



mainOrders = orderData["mainOrders"]
mainOrders_str = json.dumps(mainOrders)



header = ['序号','日期','商家','商品名','总价','价格']
csvfile=open('taobao_orderData_test3.csv', 'w')

# csvfile = file('taobao_orderData.csv', 'wb')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(header)

# i = 1
# for item in mainOrders :
#     orderCreateTime = item["orderInfo"]["createDay"] # 订单产生时间
#     shopName = item["seller"]["shopName"] # 商家名称
#     orderFee = item["payInfo"]["actualFee"] # 订单总金额
#     newrow = [i,orderCreateTime,shopName,'' ,orderFee,''] # 构造打印列
#     csvwriter.writerow(newrow)
#     i = i + 1
#     for suborder in item["subOrders"] :
#         merchandiseName = suborder["itemInfo"]["title"] # 商品名
#         merchandisePrice = suborder["priceInfo"]["realTotal"] # 商品价格
#         newrow = ['','','',merchandiseName,'',merchandisePrice] # 构造打印列
#         csvwriter.writerow(newrow)
fileList = traversalFiles.walkFile("taobao-orders")

for item in fileList :
    orderDataParse.dataParse(item,'taobao_orderData_test3.csv')



# 数据汇总 是第一步需要做的,第二步再做数据聚合


