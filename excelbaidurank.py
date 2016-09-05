#!/usr/local/bin/python
#-*-coding:utf-8-*-

import xdrlib
import sys
import xlrd
from pmchaxun import BaiduRank
from xlutils.copy import copy
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

baidurank = BaiduRank()

# domain = 'www.jmtyzs.net/'  # set the domain which you want to search.
# checkWord = '南昌庭院装饰'
# rank = baidurank.getRank(checkWord, domain)
# print rank
# 打开excel 文件
data = xlrd.open_workbook('paimincx.xls')
# 通过名称获取工作表
table = data.sheet_by_name(u'Sheet1')
# 获取表格的行数和列数
nrows = table.nrows
ncols = table.ncols
cxwz_data = []
cxgjc_data = []
gjcpm_data = []
rowrank = []
rowrankall = []
for i in range(nrows):
    # 获取一行的数据，返回数组
    row_values = table.row_values(i)
    cxwz_data.append(row_values[0])
    cxgjc_data.append(row_values[1])
    gjclist = cxgjc_data[i]
    m = re.split(',', gjclist)
    gjcpm_data.append(m)
    for a in range(0, len(gjcpm_data[i])):
        rank = baidurank.getRank(
            gjcpm_data[i][a].encode('utf-8'), cxwz_data[i])
        print rank
        oldWb = xlrd.open_workbook('paimincx.xls', formatting_info=True)
        newWb = copy(oldWb)
        newWs = newWb.get_sheet(0)
        newWs.write(i, 2+a, "%s" % unicode(rank))
        print "write new values ok"
        newWb.save('paimincx.xls')
        print "save with same name ok"

# print gjcpm_data[0][1]
# oldWb = xlrd.open_workbook('paimincx.xls', formatting_info=True)
# newWb = copy(oldWb)
# newWs = newWb.get_sheet(0)
# newWs.write(1, 0, "value1")
# newWs.write(1, 1, "value2")
# newWs.write(1, 2, "value3")
# print "write new values ok"
# newWb.save('paimincx.xls')
# print "save with same name ok"
