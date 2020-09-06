import os
import winreg

#判断回收站目录是否存在
def returnDir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled', 'C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

#通过sid获取用户名信息
def sid2user(sid):
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\\" + sid)
        #获取该目录下所有键的个数: 0-下属键个数; 1-当前键值个数
        count = winreg.QueryInfoKey(key)[1] 
        for j in range(count):
            #FileNotFoundError: [WinError 2] 系统找不到指定的文件
            #(value, type) = winreg.QueryValue(key, 'ProfileImagePath')
            name, value, type = winreg.EnumValue(key, j)
            if('ProfileImagePath' in name):
                user = value.split('\\')[-1]
                #print(user)
        return user
    except:
        return sid

#获取回收站内容
def findRecycle(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        print(sid)
        files = os.listdir(recycleDir+sid)
        print(files)
        user = sid2user(sid)
        print('[*]Listing Files For User:' + str(user))
        for file in files:
            print('[+]Found File:' + str(file))
        print("")

#主函数
def main():
    res = returnDir()
    print(res)             #C:\$Recycle.Bin
    findRecycle(res)
    
if __name__ == '__main__':
    main()

