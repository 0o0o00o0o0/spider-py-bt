#coding=utf-8
from app import app
from app.connect import ConnectDb
from flask import request
from bs4  import BeautifulSoup
import sys
import time
import socket
reload(sys)
sys.setdefaultencoding( "utf-8" )
connectdbobect = ConnectDb('localhost','root','zhangshuan','mysql',3306)
import urllib2

baseUrl = "http://www.ciliba.xyz"
uploading = False
def getUrl(url):
    return baseUrl + "/s/%s.html" %url

@app.route('/index', methods=['GET'], endpoint="index")
def m():
    result = connectdbobect.selectDb('select * from  user')
    # print result
    return {"a":4}

def getBt(url):
    try:
        req = urllib2.Request(url)
        # 模仿火狐浏览器
        req.add_header("user-agent", "Mozilla/5.0")
        response = urllib2.urlopen(req,timeout=10)
        code = response.getcode()
        content = response.read()
        # print content
        if code == 200 :
            soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
            return soup.find('a',class_="download").get('href')
        return ''
    except socket.timeout as e:
        return ''
    except urllib2.HTTPError as e:
        return ''

def spider(url,nums,id):
    try:
        number = nums
        sql = "INSERT INTO search_content (id,name,url,type,time,file,hot) values ('%s'" %id
        req = urllib2.Request(url)
        # 模仿火狐浏览器
        req.add_header("user-agent", "Mozilla/5.0")
        response = urllib2.urlopen(req,timeout=10)
        code = response.getcode()
        content = response.read()
        # print content
        if code == 200 :
            soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
            search_item = soup.find_all('div',class_="search-item")
            for item in search_item:
                number = number - 1
                upsql = sql +",'%s'" %item.h3.get_text()
                upsql = upsql +",'%s'" %getBt(baseUrl+ item.h3.a.get('href'))
                for span in item.find('div',class_="item-bar").find_all('span'):
                    auu = span.get_text().split(':')
                    if len(auu) == 2:
                        upsql=upsql+",'%s'" %auu[1]
                    else:
                        upsql=upsql+",'%s'" %auu[0]
                upsql = upsql +");"
                print upsql
                try:
                    connectdbobect.updateDb(upsql)
                except:
                    print 'error'
                time.sleep(2)
            if number > 0 and soup.find('li',class_="nextpage"):
                spider(baseUrl+ soup.find('li',class_="nextpage").a.get('href'),number,id)
    except  Exception as e:
        print e

@app.route('/search', methods=['GET'], endpoint="search")
def s():
    args = request.args
    url = getUrl(args['name'])
    nums = args['num'] if 'num' in args else 1000
    sql = "select * from search_item where content = '%s'" %args['name']
    result = connectdbobect.selectDb(sql)
    print result
    if len(result)>0:
        return {"err":"已经搜索过了"}
    usql = "INSERT INTO search_item (content) values ('%s')" %args['name']
    connectdbobect.updateDb(usql)
    nresult = connectdbobect.selectDb(sql)
    spider(url,nums,nresult[0][0])
    return {'yy':4}