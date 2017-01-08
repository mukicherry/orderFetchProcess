# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json


# header = ['文件序号','序号','日期','商家','商品名','总价','价格']
# 这里需要把cswriter传入,否则会出现写文件断掉的情况
def dataParse(csvwriter,fileIndex,fileName,outFileName):
    with open(fileName, 'r') as file:
        orderData = json.load(file)

    mainOrders = orderData["mainOrders"]

    newrow = [fileIndex]
    csvwriter.writerow(newrow)
    i = (fileIndex-1)*15 + 1
    for item in mainOrders:
        orderCreateTime = item["orderInfo"]["createDay"]  # 订单产生时间
        shopName = item["seller"]["shopName"]  # 商家名称
        orderFee = item["payInfo"]["actualFee"]  # 订单总金额
        newrow = [' ', i, orderCreateTime, shopName, ' ', orderFee, ' ']  # 构造打印列
        csvwriter.writerow(newrow)
        i = i + 1
        for suborder in item["subOrders"]:
            merchandiseName = suborder["itemInfo"]["title"]  # 商品名
            merchandisePrice = suborder["priceInfo"]["realTotal"]  # 商品价格
            newrow = [' ',' ', ' ', ' ', merchandiseName, ' ', merchandisePrice]  # 构造打印列
            csvwriter.writerow(newrow)