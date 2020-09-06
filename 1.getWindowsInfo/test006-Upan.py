# encoding:utf-8
from winreg import *
import sys

usb_name = []
uid_flag = []
usb_path = []

#连接注册表根键 以HKEY_LOCAL_MACHINE为例
regRoot = ConnectRegistry(None, HKEY_LOCAL_MACHINE)

#检索子项
subDir = r"SYSTEM\CurrentControlSet\Enum\USBSTOR"

#获取指定目录下所有键的控制
keyHandle = OpenKey(regRoot, subDir)

#获取该目录下所有键的个数(0-下属键个数 1-当前键值个数)
count = QueryInfoKey(keyHandle)[0]
print(count)

#穷举USBSTOR键获取键名
for i in range(count):
    subKeyName = EnumKey(keyHandle, i)
    subDir_2 = r'%s\%s' % (subDir, subKeyName)
    #print(subDir_2)

    #根据获取的键名拼接之前的路径作为参数 获取当前键下所属键的控制
    keyHandle_2 = OpenKey(regRoot, subDir_2)
    num = QueryInfoKey(keyHandle_2)[0]
    #遍历子键内容
    for j in range(num):
        subKeyName_2 = EnumKey(keyHandle_2, j)
        #print(subKeyName_2)
        result_path = r'%s\%s' % (subDir_2, subKeyName_2)

        #获取具体键值内容并判断Service为disk
        keyHandle_3 = OpenKey(regRoot, result_path)
        numKey = QueryInfoKey(keyHandle_3)[1]
        for k in range(numKey):
            #获取USB名称
            name, value, type_ = EnumValue(keyHandle_3, k)
            if(('Service' in name) and ('disk'in value)):
                value,type_ = QueryValueEx(keyHandle_3,'FriendlyName')
                usb = value
                uid = subKeyName_2
                path = "USBSTOR" + "\\" + subKeyName + "\\" + subKeyName_2
                print(usb)
                print(uid)
                print(path)                
                print("")
    
#关闭键值
CloseKey(keyHandle)
CloseKey(regRoot)


