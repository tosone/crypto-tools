# -*- coding: utf-8 -*-  
import urllib2  
import urllib  
import json 
import re
import hashlib 
import sys  
from HTMLParser import HTMLParser  
from htmlentitydefs import entitydefs  
reload(sys)  
sys.setdefaultencoding('utf-8')  
  
class titlehtml(HTMLParser):  


   

    def __init__(self):  
        self.title=[]  
        self.readingtitle=''  
        self.myfilter=''  
        HTMLParser.__init__(self)  
    def handle_starttag(self, tag, attrs):  
        if tag==self.myfilter:  
            self.readingtitle=1  
    def handle_data(self, data):  
        if self.readingtitle:  
            self.title.append(data)  
    def handle_endtag(self, tag):  
        if tag==self.myfilter:  
            self.readingtitle=0  
  
    def gettile(self):  
        return self.title  
  
class MyHTMLParser(HTMLParser):  
    def __init__(self):  
        HTMLParser.__init__(self)  
        self.inputvalue = {}  
  
    def handle_starttag(self, tag, attrs):  
        #print "Encountered the beginning of a %s tag" % tag  
        if tag == "input":  
            if len(attrs) == 0: pass  
            else:  
                for (variable, value)  in attrs:  
  
                    if variable=="name":  
                        self.inputvalue.setdefault(value,'')  
                        myname=value  
                    if variable == "value":  
                        self.inputvalue[myname]=value  
  
def httpget(geturl,getdata,Referer):  
    urldata=urllib.quote(getdata)  
    url=geturl+urldata  
    headers={"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1","Referer":Referer}  
    req = urllib2.Request(url,headers=headers)  
    resul=urllib2.urlopen(req).read()  
    return resul  
  
def httppost(geturl,getdata,Refererdata):  
    data=getdata  
    url=geturl  
    post_data=urllib.urlencode(data)  
    headers={"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1","Referer":Refererdata}  
    req=urllib2.Request(url,headers=headers,data=post_data)  
    resul=urllib2.urlopen(req).read()  
    return resul


  
  
def cmd5(md5):  
    data="" 
    try:  
        res=httpget("http://www.cmd5.com/",data,"")
        viewstaut=MyHTMLParser()
    except urllib2.URLError:  
        print '[+] site: http://www.cmd5.com/ \t\t\t\t[+] Error: seems to be down'
        return 0  
    viewstaut.feed(res)  
    post_data=viewstaut.inputvalue  
    post_data["ctl00$ContentPlaceHolder1$TextBoxInput"]=md5  
    post_data["__EVENTTARGET"]=""  
    post_data["ctl00$ContentPlaceHolder1$InputHashType"]="md5"  
    post_data["ctl00$ContentPlaceHolder1$HiddenField1"]="0"  
    finres=httppost("http://www.cmd5.com/",post_data,"http://www.cmd5.com/")  
    newsparser = titlehtml()  
    newsparser.myfilter='span'  
    newsparser.feed(finres)  
    items = newsparser.gettile()  
    if len(items)==0:  
        print u"[-] site: http://www.cmd5.com/\t\t\t没有查到"  
    else:  
        print u"[-] site: http://www.cmd5.com/\t\t\t查到的结果是："+items[3]  
  
  
def syue(md5):
    try:  
        finstr=httpget("http://md5.syue.com/ShowMD5Info.asp?GetType=ShowInfo&md5_str=",md5,"http://md5.syue.com/")  
    except urllib2.URLError:  
        print '[+] site: http://www.cmd5.com/ \t\t\t\t[+] Error: seems to be down'
        return 0 
    newsparser = titlehtml()  
    newsparser.myfilter='span'  
    newsparser.feed(finstr)  
    items = newsparser.gettile()  
    try:  
        print u"[-] site: http://md5.syue.com/\t\t\t查询的结果是："+items[0]  
    except:  
        print u"[-] site: http://md5.syue.com/\t\t\t没有查到"  
  
def pmd5(md5):  
    data=""  
    try: 
        res=httpget("http://pmd5.com/",data,"")
    except urllib2.URLError:  
        print '[+] site: http://www.cmd5.com/ \t\t\t\t[+] Error: seems to be down'
        return 0 
    viewstaut=MyHTMLParser()  
    viewstaut.feed(res)  
    post_data=viewstaut.inputvalue  
    post_data["key"]=md5  
    finres=httppost("http://pmd5.com/",post_data,"http://pmd5.com/")  
    newsparser = titlehtml()  
    newsparser.myfilter='em'  
    newsparser.feed(finres)  
    items = newsparser.gettile()  
    try:  
        print u"[-] site: http://pmd5.com/\t\t\t查找的结果是："+items[1]  
    except:  
        print u"[-] site: http://pmd5.com/\t\t\t没有查到"  



  
def wmd5(md5):  
    url="http://www.wmd5.com/ajax.php"  
    data={}  
    #data["miwen"]=md5  
    #data["action"]="md5show"
    data = urllib.urlencode({'miwen':md5,'action':'md5show'}) 
    #finstr=httppost(url,data,"http://www.wmd5.com/")

    try:    
        req = urllib2.Request(url)
        fd = urllib2.urlopen(req, data)   
        d1 = fd.read()
        #d1=json.JSONDecoder().decode(finstr) 
        a = eval(d1)
        #dictinfo = simplejson.loads(json_str)
    
        if  a['status'] == 'success' :print u'[-] site: http://www.wmd5.com/\t\t\t查询的结果是：'+str(a['md5text'])  
        else: print u'[-] site: http://www.wmd5.com/\t\t\t没有查到' 
    except urllib2.URLError:  print '[+] site: %s \t\t\t[+] Error: seems to be down' % url

def myaddr(passwd):
    site = 'http://md5.my-addr.com/'
    rest = 'md5_decrypt-md5_cracker_online/md5_decoder_tool.php'
    para = urllib.urlencode({'md5':passwd})
    req  = urllib2.Request(site+rest)
    try:
      fd   = urllib2.urlopen(req, para)
      data = fd.read()

      match= re.search('(Hashed string</span>: )(\w+.\w+)', data)
      if match: print u'[-] site: %s\t\t查找的结果是：%s' % (site, match.group(2))
      else: print u'[-] site: %s\t\tPassword: Not found' % site
    except urllib2.URLError:  print '[+] site: %s \t\t\t[+] Error: seems to be down' % site


    
def rednoize(passwd):
    site = 'http://hashtoolkit.com/'
    para = 'reverse-hash/?hash=' + passwd
    try:
      reqq = site+para
      headers = {'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}  
      reqa = urllib2.Request(url=reqq,headers=headers)  
      req = urllib2.urlopen(reqa)

      data = req.read()
	  
      match = re.search(r'(Hashes for: <code>)(.+[^>])</code></h1></div>', data)
      if match: print u'[-] site: %s\t\t查找的结果是：%s' % (site, match.group(2))
      else: print u'[-] site: %s\t\tPassword: Not found' % site
    except urllib2.URLError: print '[+] site: %s \t\t\t[+] Error: seems to be down' % site


     
def md5decryption(passwd):
    site = 'http://md5decryption.com/'
    para = urllib.urlencode({'hash':passwd,'submit':'Decrypt+It!'})
    req = urllib2.Request(site)
    try:
      fd = urllib2.urlopen(req, para)
      data = fd.read()
      match = re.search(r'(Decrypted Text: </b>)(.+[^>])(</font><br/><center>)', data)
      if match: print u'[-] site: %s\t\t查找的结果是：%s' % (site, match.group(2))
      else: print u'[-] site: %s\t\tPassword: Not found' % site
    except urllib2.URLError: print '[+] site: %s \t\t\t[+] Error: seems to be down' % site   
 
  
  
  
if __name__=='__main__':  
    md5=sys.argv[1]  
    #print md5  

    #md5="d8b521d9c8591a897704b83d18ec988d"
    md5decryption(md5)
    cmd5(md5)
    #nmd5(md5) 
    rednoize(md5)
    myaddr(md5) 
    wmd5(md5)  
    pmd5(md5) 
    syue(md5)   