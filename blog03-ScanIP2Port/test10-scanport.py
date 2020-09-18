# -*- coding: utf-8 -*-
import telnetlib

#端口扫描
def get_ip_status(ip,port):
    server = telnetlib.Telnet()      #创建一个Telnet对象
    try:
        server.open(ip,port)         #利用Telnet对象的open方法进行tcp链接
        print('{0} port {1} is open'.format(ip, port))
    except Exception as err:
        print('{0} port {1} is not open'.format(ip,port))
    finally:
        server.close()
 
if __name__ == '__main__':
    host = '210.40.81.16'
    for port in range(20,100):
        get_ip_status(host,port)
