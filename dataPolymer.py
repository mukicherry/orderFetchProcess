# -*- coding: utf-8 -*-
#!/usr/bin/python
# 数据聚合类
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv
import orderDataParse
import traversalFiles



header = ['文件序号','序号','日期','商家','商品名','总价','价格']
csvfile=open('taobao_order_2016.csv', 'w')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(header)



fileList = traversalFiles.walkFile("taobao-orders")

i = 1
for item in fileList :
    orderDataParse.dataParse(csvwriter,i,item,'taobao_order_2016.csv')
    i = i + 1






