import sys 
import urllib ,urllib2 
import re

def baidu(w,pn):
    '''返回当前页的内容''' 
    url= "http://www.baidu.com/s?"
    values = {
    "w":w.encode('gbk','ignore'), 
    "pn":pn
    } 
    data = urllib.urlencode(values)
    newurl = url + data
    response = urllib2.urlopen(newurl) 
    the_page = response.read()
    return the_page 

def ana(data,mysite,pn):
    '''检测关键字的位置''' 
    o = re.compile(r'href="(.+?)"')
    f = o.findall(data) 
    line = pn
    for ff in f:
        ff = ff.strip()  
        if not re.search("^s\?",ff) and re.search("^http:\/\/",ff) and not re.search('baidu.com',ff):
            if re.search(mysite,ff): 
                print "* " ,line ,ff
                return True 
            else:
                print line,ff 
                line = line + 1
                continue 
         
    
if __name__ == "__main__": 
    mysite = sys.argv[2]
    pn = 1
    while True:
        keyword = sys.argv[1].decode('gbk')
        data = baidu(keyword,pn) 
        checkflag = ana(data,mysite,pn)
        if not checkflag:
            pn = pn + 10
            print "page %s" % str(int(pn)/10)
        else:
            print 'found:%s' % (mysite)
            break
    else:
        print 'not found:%s' % (mysite)