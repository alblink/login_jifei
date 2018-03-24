# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/24 12:02
@Author  : YeJian
@File    : test.py

"""

import urllib.request
from bs4 import BeautifulSoup
import re

# url = 'http://172.16.6.3'
# res = urllib.request.urlopen(url)
# html = res.read().decode('gbk')
# soup = BeautifulSoup(html, 'html.parser')
#
# print(soup.title.get_text())


url = 'http://172.16.6.3'
res = urllib.request.urlopen(url)

html = res.read().decode('gbk')
t = re.compile(r'"已使用流量.+?"')
print(re.findall(t, html))


