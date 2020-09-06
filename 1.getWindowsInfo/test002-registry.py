# encoding:utf-8
from winreg import *
import sys

#连接注册表根键 以HKEY_LOCAL_MACHINE为例
regRoot = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
subDir = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList'

#获取指定目录下所有键的控制
keyHandle = OpenKey(regRoot, subDir)

#获取该目录下所有键的个数(0-下属键个数 1-当前键值个数)
count = QueryInfoKey(keyHandle)[0]
for i in range(count):
    #穷举键获取键名
    subKeyName = EnumKey(keyHandle, i)
    subDir_2 = r'%s\%s' % (subDir, subKeyName)
    
    #根据获取的键名拼接之前的路径作为参数 获取当前键下所属键的控制
    keyHandle_2 = OpenKey(regRoot, subDir_2)
    num = QueryInfoKey(keyHandle_2)[1]
    for j in range(num):
        name, value, type_ = EnumValue(keyHandle_2, j)
        if('ProfileImagePath' in name and 'Users' in value):
            print(value)
    #读写操作结束后关闭键
    CloseKey(keyHandle_2)
    
CloseKey(keyHandle)
CloseKey(regRoot)
