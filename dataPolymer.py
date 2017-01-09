# -*- coding: utf-8 -*-
#!/usr/bin/python
# 数据聚合类
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv
import orderDataParse
from utils import traversalFiles

header = ['文件序号','序号','日期','商家','商品名','总价','价格']
preprocessResultFileName = '/Users/CherryMuki/workspace/orderFetchProcess/preprocessResult/taobao_order_2016_1.csv'
csvfile=open(preprocessResultFileName, 'w')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(header)


fileList = traversalFiles.walkFile("/Users/CherryMuki/workspace/orderFetchProcess/datafetch/taobao-orders")

i = 1
for item in fileList :
    orderDataParse.dataParse(csvwriter, i, item, preprocessResultFileName)
    i = i + 1






