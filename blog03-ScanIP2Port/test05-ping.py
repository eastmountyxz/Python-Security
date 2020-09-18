# -*- coding: utf-8 -*-
import time
from subprocess import Popen, PIPE

def ping_check():
    ip = '127.0.0.1'
    check = Popen("ping {0} \n".format(ip), stdin=PIPE, stdout=PIPE,  shell=True)
    data = check.stdout.read() #数据
    data = data.decode("gbk")  #编码转换:byte->str
    if 'TTL' in data: #存活
        print('UP')

#程序成功在同一时刻运行两个函数
if __name__ == '__main__':
    ping_check()
