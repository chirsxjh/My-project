#-*-coding:utf-8-*-
import requests
import  urllib2
from bs4 import BeautifulSoup
from lxml import etree
from lxml import etree
import os
from PIL import Image
import pdb
from ZFCheckCode import recognizer
from ZFCheckCode import trainner 


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Referer': 'http://jwgl1.hbnu.edu.cn/(S(nxuiogv1kq4coqvvhltax145))/default2.aspx?'
}

baseurl = 'http://jwgl1.hbnu.edu.cn'
s=requests.Session()
html = s.get(baseurl, headers=headers, allow_redirects=False )
loc = html.headers['location']
loginurl = baseurl + loc
codeu = loginurl[0:54]
codeurl = codeu + '/CheckCode.aspx?'

def checkcode():
    img=s.get(codeurl, stream=True, headers=headers)
    with open('checkcode.gif','wb') as f:
        f.write(img.content)
    trainner.update_model() 
    code = recognizer.recognize_checkcode('/home/xiang/workspace/checkcode.gif')
    print(code)
    return code



def login(id, passwd):
    #构造表单字典
    payload={'__VIEWSTATE':'',
        'txtUserName':'',
        'Textbox1':'',
        'TextBox2':'',
        'txtSecretCode':'',
        'RadioButtonList1':'',
        'Button1':'',
        'lbLanguage':'',
        'hidPdrs':'',
        'hidsc':'',
        '__EVENTVALIDATION':'',
        }
    
    #获取表单字典数据
    index = s.get(loginurl, headers=headers)
    soup = BeautifulSoup(index.content,'lxml')
    value1=soup.find('input',id='__VIEWSTATE')['value']
    value2=soup.find('input',id='__EVENTVALIDATION')['value']
    payload['txtUserName']=id
    payload['TextBox2']=passwd
    code = checkcode()
    payload['txtSecretCode']= code
    payload['RadioButtonList1']=u"学生".encode('gb2312','replace')
    payload['__VIEWSTATE']=value1       
    payload['__EVENTVALIDATION']=value2 
    payload['RadioButtonList1']= '%D1%A7%C9%FA' 

    loginresponse = s.post(loginurl, data=payload, headers=headers)
    content = loginresponse.content.decode('gb2312')
    soup = BeautifulSoup(content, 'lxml')
    uname=soup.find('span', id='xhxm')
    xsxm =  uname.text

    return xsxm




def getgrades(id, passwd):

    payload1={'__VIEWSTATE':'',
          'ddlXN':'', 
          'ddlXQ':'' ,
          'Button1':'',
          '__EVENTVALIDATION':'',

}
    url2 = login(id, passwd)
    name = url2[0:9]
    cname = urllib2.quote(name.encode('gb2312'))
    xingming = urllib2.quote(cname) 
    
    req_url = codeu + '/xscj_gc.aspx?xh=' + id + '&xm=' + xingming + '&gnmkdm=N121603'
    req2 = s.get(req_url, headers=headers)

    soup = BeautifulSoup(req2.content,'lxml')
    value3=soup.find('input',id='__VIEWSTATE')['value']
    value4=soup.find('input',id='__EVENTVALIDATION')['value']
    payload1['__VIEWSTATE']=value3
    payload1['__EVENTVALIDATION']=value4

    pos = s.post(req_url, data=payload1, headers=headers)
    grades = pos.content.decode('gbk')
    
    return grades

if __name__ == __main__ :
    a = raw_input('学号：')
    b = raw_input('密码：')
    score = getgrades(a, b)
    print score
    