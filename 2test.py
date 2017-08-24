
# -*- coding: utf-8 -*-
'''
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
			'fastloginfield':'username',
			'username':'2382614177',
            'password':'6ad1262346973b9f9f5bef2082f86754',
            'quickforward':'yes',
            'handlekey':'ls'
		})
#登录教务系统的URL
loginUrl = 'http://aaa.yldt.in/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://aaa.yldt.in'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()
'''

# -*-coding:UTF-8-*-
import urllib
import urllib2
import os
from lxml import etree
def allurl():
    url = 'http://www.mzitu.com/all'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0','Referer': 'http://www.mzitu.com'}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request).read()
    #print response
    pattern = etree.HTML(response)
    link_list = pattern.xpath('//a[@target="_blank"]/@href')
    for link in link_list:
        #girlurl(link,headers)
        link = link
        girlurl(link,headers)

def girlurl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    #print response
    pattern = etree.HTML(response)
    #dirName = pattern.xpath('//head[1]/title/text()')
    #for ccc in dirName:
    #    DIRNAME = ccc.encode('utf-8')
    pattern = etree.HTML(response)
    link_list = pattern.xpath('//div[@class="pagenavi"]/a[5]/span/text()')
    for num in link_list:
        #print num
        for Num in range(1,int(num)):
            Newurl = url +  '/' + str(Num)
            #print Newurl
            lasturl(Newurl,headers)

    #for link in link_list:
    #    print link
def lasturl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    pattern = etree.HTML(response)
    link_list = pattern.xpath('//div[@class="main-image"]/p/a/img/@src')
    #dirName = pattern.xpath('//head[1]/title/text()')
    #print dirName.encode("UTF-8")
    #for bbb in dirName:
    #    print bbb.encode("UTF-8")
    #print link_list
    for link in link_list:
        #print link
        saveimg(link,headers)
def saveimg(url,headers):
    #dir = os.mkdir(str(name))
    #print dir
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    print url[-9:]
    #DIR = '/Users/cgs/cgs/Desktop/' + dir + url[-9]
    #print DIR
    with open('/Users/cgs/cgs/Desktop/' + url[-9:],'wb') as f:
        f.write(response)




allurl()

'''
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' +
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        haveImg = re.search("img", item[3])
        if not haveImg:
            print item[0], item[1], item[2], item[4]
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
'''

