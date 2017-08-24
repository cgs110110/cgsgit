
#coding=utf-8  
import urllib2  

oldurl = "http://www.lesmao.com/portal.php?page="
for a in range(2,200):
    url = oldurl + str(a)
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0","Referer":"http://www.lesmao.com/"}
    request = urllib2.Request(url,headers = headers)
    try:  
        response = urllib2.urlopen(request)  
        print response.read( )  
        response.close( )  
    
    except urllib2.URLError, e:  
        if hasattr(e, "reason"):  
            print "Failed to reach the server"  
            print "The reason:", e.reason  
        elif hasattr(e, "code"):  
            print "The server couldn't fulfill the request"  
            print "Error code:", e.code  
            print "Return content:", e.read()  
        
