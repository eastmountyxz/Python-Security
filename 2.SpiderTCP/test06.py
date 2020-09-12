# -*- coding:utf-8 -*-
import urllib.request

url = "http://www.baidu.com"
content = urllib.request.urlopen(url)
print(content.info())        #头信息
print(content.geturl())      #请求url
print(content.getcode())     #http状态码
