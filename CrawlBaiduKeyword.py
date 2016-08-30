#!/usr/local/bin/python
#-*-coding:utf-8-*-
# 2015-6-26 DaoXin
import pycurl
import StringIO
import urllib
import urllib2
from random import choice
import re
import sys
import string
from bs4 import BeautifulSoup
import requests
import csv
import xlrd
import xlwt
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# useragent 列表，大家可以自行去收集。不过在本例中似乎不需要这个
AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
    "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-CN) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; zh-CN) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; zh-CN) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.5 (KHTML, like Gecko) Safari/312.3",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Camino/2.2.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre Camino/2.2a1pre",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML like Gecko) Chrome/22.0.1229.79 Safari/537.4",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; zh-CN) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0.112941",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; zh-CN) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0",
]


class CrawlBaidukeyword:

    def __init__(self):
        self.UserAgent = choice(AGENTS)

    def curl(self, url, headers):
        while 1:
            try:
                c = pycurl.Curl()
                c.setopt(pycurl.MAXREDIRS, 5)
                c.setopt(pycurl.REFERER, url)
                c.setopt(pycurl.FOLLOWLOCATION, True)
                c.setopt(pycurl.CONNECTTIMEOUT, 120)
                c.setopt(pycurl.TIMEOUT, 120)
                c.setopt(pycurl.ENCODING, 'gzip,deflate')
                # c.setopt(c.PROXY,ip)       '''若使用代理，则取消本行注释'''
                c.fp = StringIO.StringIO()
                c.setopt(pycurl.URL, url)
                c.setopt(pycurl.HTTPHEADER, headers)
                c.setopt(pycurl.USERAGENT, self.UserAgent)
                c.setopt(c.WRITEFUNCTION, c.fp.write)
                c.perform()
                # code = c.getinfo(c.HTTP_CODE) 返回状态码
                html = c.fp.getvalue()
                if '="http://verify.baidu.com' in html:
                    print '出验证码,暂停10分钟'
                    time.sleep(1200)
                    continue
                else:
                    return html
            except Exception, what:
                information = '错误信息：%s' % what
                return str(information)
                continue

    def baiduindexcombobox(self, guanjianmuci):
        baiduindex_data = []
        baiduurl = "http://nssug.baidu.com/su?prod=index&wd=" + \
            urllib.quote(guanjianmuci)
        pagehtml = self.curl(baiduurl)
        if "p:false," in pagehtml:
            cwguanjiancilist = re.findall(r"\"(.*?)\"", pagehtml)
            del cwguanjiancilist[0]
            for cwguanjianci in cwguanjiancilist:
                baiduindex_data.append(cwguanjianci)

        return baiduindex_data

    def baidurightrelatedsearch(self, cppagehtml):
        rightrelatedsearch_data = []

        baidurightsoup = BeautifulSoup(cppagehtml, "lxml")
        zchtml = baidurightsoup.find_all(
            "div", class_="opr-recommends-merge-panel opr-recommends-merge-mbGap")

        for chanpinbt in zchtml:
            zchtml1 = chanpinbt.select(
                "[class~=c-gap-top-small] a")
            for chanpinbt in zchtml1:
                rightrelatedsearch_data.append(chanpinbt.string)

        return rightrelatedsearch_data

    def index5118(self, pagehtml):
        keywordindex_data = []
        keywordssnum_data = []

        soup = BeautifulSoup(pagehtml, "lxml")
        keywordindexhtml = soup.select(
            "[class~=Fn-ui-list] dl:nth-of-type(2) dd:nth-of-type(2)")
        for keywordindex in keywordindexhtml:
            keywordindex_data.append(keywordindex.string)

        keywordssnumhtml = soup.select(
            "[class~=Fn-ui-list] dl:nth-of-type(2) dd:nth-of-type(3)")
        for keywordssnum in keywordssnumhtml:
            keywordssnum_data.append(keywordssnum.string)

        data5118_data = [keywordindex_data, keywordssnum_data]

        return keywordindex_data

    def socombobox(self, guanjianmuci):
        socombobox_data = []
        baiduurl = "https://sug.so.360.cn/suggest?callback=suggest_so&encodein=utf-8&encodeout=utf-8&format=json&fields=word,obdata&word=" + \
            urllib.quote(guanjianmuci)
        pagehtml = self.curl(baiduurl)
        if "\"result\":[]" not in pagehtml:
            cwguanjiancilist = re.findall(r"\"word\":\"(.*?)\"}", pagehtml)
            for cwguanjianci in cwguanjiancilist:
                socombobox_data.append(cwguanjianci)

        return socombobox_data

    def sogoucombobox(self, guanjianmuci):
        sogoucombobox = []
        baiduurl = "https://www.sogou.com/suggnew/ajajjson?key=" + \
            urllib.quote(guanjianmuci) + "&type=web"
        pagehtml = self.curl(baiduurl)
        if "[],[],[]," not in pagehtml:
            cwguanjiancilist = re.findall(
                r"sug\([\".*\",[(.*)\"],[\"0;", pagehtml)
            for cwguanjianci in cwguanjiancilist:
                sogoucombobox.append(cwguanjianci)

        return sogoucombobox
