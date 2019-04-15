#_*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
from lxml import etree
import pdb
import os
import commands
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

s = requests.get('https://blog.csdn.net/weixin_42595331/article/details/88950493')
print s.text

'''
def connecturl(kword):
    url = 'https://so.csdn.net/so/search/s.do?q=' + kword
    return url


def get_keyword(inf):
    search_results = []
    url = connecturl(inf)
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    s = html.text
    soup = BeautifulSoup(s, 'html.parser')

'''