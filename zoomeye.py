# _*_ coding:utf-8 _*_
import urllib2
import json
import urllib
#获取access_token值
def take_token(url,headers,data):
    #将数据转换成json格式
    data_encode = json.dumps(data)
    request = urllib2.Request(url,data_encode,headers = headers)
    response = urllib2.urlopen(request)
    #将数据转换成python格式
    token = json.loads(response.read())
    #声明一个access_token全局变量
    global access_token87u
    access_token = token['access_token']
    #print access_token
    resources_info()
def resources_info():
    global access_token
    print access_token
    headers1 = {"Authorization":"JWT" + access_token}
    request = urllib2.Request("https://api.zoomeye.org/resources-info",headers = headers1)
    response = urllib2.urlopen(request)
    print response.read()


if __name__=="__main__":
    url = "https://api.zoomeye.org/user/login"
    data = {"username":"2382614177@qq.com","password":"cgs110110"}
    User_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
    headers = {"User-Agent": User_agent}
take_token(url,headers,data)

