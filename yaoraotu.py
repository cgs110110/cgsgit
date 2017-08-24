# _*_ coding:utf-8 _*_
import urllib
import urllib2
import re
from lxml import etree

def allurl(url,headers):
    for a in range(1,287):
        Newurl = url + str(a) +'.html'
        print Newurl
        request = urllib2.Request(Newurl, headers=headers)
        response = urllib2.urlopen(request).read()
        pattern = etree.HTML(response)
        link_list = pattern.xpath('//div[@id="colmain"]/div[1]/ul/li/a/@href')
        #print link_list
        for link in link_list:
            allgirl(link,headers = headers)
def allgirl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    pattern = etree.HTML(response)
    link_num = pattern.xpath('//div[@class="pages listpage"]/a[7]/@href')
    #print link_num

    for num in link_num:
        Oldnum = str(num).split('_')[1]
        Newnum = Oldnum.split('.')[0]
        #print Newnum
        allimgurl(Newnum,url,headers)

def allimgurl(num,url,headers):
    for Num in range(1,int(num)):
        Newurl = url[:-5] + '_' + str(Num) + '.html'
        #print Newurl
        getimgurl(Newurl,headers)
def getimgurl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    pattern = etree.HTML(response)
    #print pattern
    link_list = pattern.xpath('//div[@class="bigpic column_5_arc"]/a/img/@src')
    name_list = pattern.xpath('//div[@class="bigpic column_5_arc"]/a/img/@alt')
    #print link_list
    for link,name in zip(link_list,name_list):
        saveimg(link,name,headers)
        print link,name
    #print link_list

def saveimg(url,name,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    with open('/home/cgs/yaoraotu/' + name,'wb') as f:
        f.write(response)




if __name__ == "__main__":
    url = "https://www.yaoraotu.com/meinv/list_"
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0","Referer":"http://www.mmonly.cc/mmtp/xgmn/175265_4.html"}

allurl(url,headers)
