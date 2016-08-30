#!/usr/local/bin/python
#-*-coding:utf-8-*-
# 2015-6-26 DaoXin
import re
from CrawlBaiduKeyword import CrawlBaidukeyword
import xlwt
from bs4 import BeautifulSoup
import urllib
import xlwt
import time
from random import choice
import urllib
import requests
from random import choice


zixungjc = open('zixungjc.html', 'a')
zixungjctxt = open('zixungjc.txt', 'a')
payload = [
    "Host: www.baidu.com",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding: gzip, deflate, br",
    # "Cookie: BAIDUID=EB6783B40738B519C9AD047EDEA7AD60:FG=1; BDUSS=ZTV2NDdmxLZ25IRzBoZm4tZ0s5Wm5tYk5UQUcyS1pSbVYtc21ycEUtUHFELXRYQVFBQUFBJCQAAAAAAAAAAAEAAABsySg3tdrSu8e5QjJCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOqCw1fqgsNXZV; BIDUPSID=791944ABF0836C124609707C4A9F9BD5; PSTM=1472430965; BD_UPN=13314352; H_PS_PSSID=1421_18559_11937_20593_20857_20732_20837_20927; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02225310500; H_PS_645EC=136eNNOMWb%2BRhqDdumIJFBz%2BIcGjC50EhCTtMBEELT%2Fcf8zPFut3cVMg9AI; BD_CK_SAM=1; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; sug=3; sugstore=1; ORIGIN=2; bdime=0"
    "Cookie:BAIDUID=EC6ED338982C9DE1ED39972F1B4E5530:FG=1; BIDUPSID=EC6ED338982C9DE1ED39972F1B4E5530; PSTM=1434515748; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a01845311744; BDUSS=35KeW10a3pvNXdNMjQyVnhLUHFoYzZUSW9EVUF-ZXE1bUNuTXFFa0hTVU1tYWhWQVFBQUFBJCQAAAAAAAAAAAEAAADLTBsKYTYzMTM4MTcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwMgVUMDIFVZ; ispeed_lsm=2; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BAIDUVERIFY=4606BC10EB2C2AB6D4B79FFA477238E38C5C6D295106222D2F75D4F8E9C766D5115D55C4E44133ACFE00D4768C6C1507E06B4C7D6221795299EE03FDE7CB2D46430000:1434541766:3f9b93890a7a5ed0; BDRCVFR[ltbVPlNi2ac]=mbxnW11j9Dfmh7GuZR8mvqV; BD_UPN=123253; sug=3; sugstore=1; ORIGIN=0; bdime=20100; H_PS_645EC=4093eiyri7wdn3v3qfviJa%2FFLXYwKxu%2FIF0wtL7d7pZ9maSmOTmtgqORRMlMRo7E; BD_CK_SAM=1; BDSVRTM=59; H_PS_PSSID=14795_1433_14602_14509_14444_14734_10812_12868_14622_14871_12723_14485_14919_14903_11664_13937_13189_10632",
    "Host:www.baidu.com",
    "Connection: keep-alive"
    "Upgrade-Insecure-Requests: 1"
]

baiduURL = "https://www.baidu.com/s?rn=50&ie=utf-8&wd=南昌麻将机"

crawlbaidukeyword = CrawlBaidukeyword()
baidusshtml = crawlbaidukeyword.curl(baiduURL, payload)
# print baidusshtml
# zixungjc.write("%s\n" % baidusshtml)
soup = BeautifulSoup(baidusshtml, 'html.parser')
# print soup
# zixungjc.write("%s\n" % soup)
# find all results in this page
results = soup.select("#content_left .c-container")
# print results
for result in results:
        # print result
        # zixungjc.write("%s\n" % result)
    checkDatalist = result.select(".c-showurl")
    for checkData in checkDatalist:
        if "<b>" in str(checkData):
            print checkData
            zixungjctxt.write("%s\n" % checkData)
        else:
            print "false"
        # print checkData.string
        # zixungjctxt.write("%s\n" % checkData.string)
