# -*- coding:utf-8 -*-
import urllib.request

url = 'https://www.baidu.com/img/bd_logo.png'
path = 'test.png'
urllib.request.urlretrieve(url, path)
