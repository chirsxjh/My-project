#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
from lxml import etree
import pdb
import os
import commands
import sys
import numpy as np

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}



def connecturl(kword):
    url = 'https://so.csdn.net/so/search/s.do?q=' + kword
    return url


def get_information(inf):
    search_results = []
    url = connecturl(inf)
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    s = html.text
    soup = BeautifulSoup(s, 'html.parser')
    i = 1
    #result = soup.find_all('div', class_ = 'limit_width')
    for result in soup.find_all('div', class_ = 'limit_width'):
        link = result.a.text
        res  = result.a['href']
        search_results.append({'title':link, 
        'url': res})
    return search_results

def addkey(leth,j):
    for i in range(1,leth+1):
        if i not in j.keys():
            j[i] = 0
    return j

#标题长度
def titie_len(inf):
    res = get_information(inf)
    shunxu = {}
    tit_len = {}
    j = 1
    for i in res:
        shunxu[j] = i['title']
        tit_len[j] = len(shunxu[j])
        #print tit_len[j]
        j = j+1
    return tit_len

#阅读数量
def read_number(inf):
    res = get_information(inf)
    link = {}
    red_num = {}
    j = 1
    for i in res:
        link[j] = i['url']
        html = requests.get(link[j], headers=headers)
        html.encoding = 'utf-8'
        s = html.text
        soup = BeautifulSoup(s, 'html.parser')
        for result in soup.find_all('span', class_ = 'read-count'):
            num = result.get_text()
            #pdb.set_trace()
            k = num[4:]
            red_num[j] = eval(k)
           
            #print red_num[j]
            j = j+1
    return red_num

#链接数量
def link_number(inf):
    res = get_information(inf)
    num_n = {}
    link = {}
    lk_num = []
    p = 1
    j = 1
    for i in res[1:]:
        link[j] = i['url']
        #print link[j]
        #pdb.set_trace()
        html = requests.get(link[j], headers=headers)
        html.encoding = 'utf-8'
        s = html.text
        soup = BeautifulSoup(s, 'html.parser')
        for result in soup.find_all('div', class_="show-content-free"):
            for k in result.find_all('a'):
                #print k['href']
                #pdb.set_trace()
                lk_num.append(k['href'])
            num_n[p] = len(lk_num)
        p = p+1
        j = j+1
           
    return num_n

#关键字次数
def words_number(inf):
    res = get_information(inf)
    link = {}
    w_number = {}
    k = 0
    j = 1
    m = 1
    for i in res[1:]:
        link[j] = i['url']
        html = requests.get(link[j], headers=headers)
        html.encoding = 'utf-8'
        s = html.text
        soup = BeautifulSoup(s, 'html.parser')
        for result in soup.find_all('div', class_ = 'recommend-box'):
            for i in result.find_all('em'):
                k = k+1
            w_number[m] = k
        m = m+1
        j = j+1
    return w_number  

#对所获取的关键字进行加权
def weighting(inf):
    wait_sort = {}
    x = titie_len(inf)
    y = read_number(inf)
    z = words_number(inf)
    w = link_number(inf)
    i = max(len(x), len(y), len(z), len(w))
    ax , ay ,az, aw = addkey(i, x), addkey(i, y), addkey(i, z), addkey(i, w)
    for j in range(1, i+1):
        elements = [ax[j], ay[j], az[j], aw[j]]
        weights = [0.4, 0.3, 0.2, 0.1]
        wait_sort[j] = int(np.average(elements, weights=weights))
    return wait_sort



#使用归并排序进行排序
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)

#输出排序好的数据
def out_put(inf):
    wait_sort = weighting(inf)
    out = []
    a = []
    #result = []
    for i in range(1, len(wait_sort)+1):
        a.append(wait_sort[i])
    a = merge_sort(a)
    #print a
    for j in range(0, len(a)):
        for i in range(1, len(wait_sort)):
            if a[j] == wait_sort[i]:
                out.append(i)
    for i in range(len(out)):
        put = get_information(inf)[out[i]]['title']
        print put 
        



    


           



    



if __name__ == "__main__":
    
    inf = raw_input('请输入关键词：')
    number = out_put(inf)
    #print number
'''
    res = get_information(inf)
    shunxu = {}
    j = 1
    for i in res:
        shunxu[j] = i['title']
        #print j,i['title'],i['url']
        print shunxu[j]
        #print len(i['title'])
        j = j+1
       
    
    cmds = ('python {}'.format(sys.argv[1]))
    result=  commands.getstatusoutput(cmds)
    #res = os.system(('python {}'.format(sys.argv[1])))
    #inf = input('请输入关键词：')
    

    #res = get_information(result)
    if result[0] == 256:
        res = get_information(result[1][40:])
        for i in res:
            print i['title'],i['url']
    else:
        print (result[1])
   '''








