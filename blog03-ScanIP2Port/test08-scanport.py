# -*- coding: utf-8 -*-
import optparse
import socket
from socket import *

#Socket连接
def connScan(tgtHost, tgtPort):
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((tgtHost, tgtPort))
        #conn.send('Violent Python\n')
        #results = conn.recv(100)
        print(' [+] %d/tcp open ' % tgtPort)
    except Exception as err:
        print(' [-] %d/tcp closed' % tgtPort)
        #print(err)
    finally:
        conn.close()
        
#扫描端口
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
        print(tgtIP)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("[+] Scan Results for: " + tgtName[0])
    except:
        print("[+] Scan Results for: " + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print(" Scanning port " + tgtPort)
        #连接端口
        connScan(tgtHost, int(tgtPort))

#主函数 optparse用于处理命令行参数
def main():
    parser = optparse.OptionParser("usage%prog "+ \
                "-H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', \
                help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', \
                help='specify target port[s] separated by comma')

    #解析脚本输入的参数值
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost==None) or (tgtPorts[0]==None):
        print('[-] You must specify a target host and port[s].')

    #端口扫描
    portScan(tgtHost, tgtPorts)
    
if __name__ == '__main__':
    main()
