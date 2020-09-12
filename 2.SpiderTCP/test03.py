# coding=utf-8  
import re  
import urllib

html = u'<title>欢迎走进Python攻防系列专栏</title>' 
title = re.findall(r'<title>(.*?)</title>', html)
for i in title:
    print(i)
