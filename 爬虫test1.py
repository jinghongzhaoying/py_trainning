# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:17:17 2017

@author: 志煜
"""

from urllib import request
from http import cookiejar
from bs4 import BeautifulSoup
url = "http://www.baidu.com"
response = request.urlopen(url)
print (response.getcode())
print(len(response.read()))
cookie = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print(cookie)
