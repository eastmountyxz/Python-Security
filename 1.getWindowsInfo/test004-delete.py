from win32com.shell import shell,shellcon
import os

debug = False
def deltoreCyclebin(filename):
    #直接删除文件，不经过回收站
    #os.remove(filename) 
    if not debug:
        #删除文件到回收站
        res = shell.SHFileOperation((0,
                                     shellcon.FO_DELETE,
                                     filename,
                                     None,
                                     shellcon.FOF_SILENT | shellcon.FOF_ALLOWUNDO | shellcon.FOF_NOCONFIRMATION,
                                     None,
                                     None))
        print(res)
        if not res[1]:
            os.system('del '+ filename)

if __name__ == '__main__':
    filename = "C:\\Users\\xiuzhang\\Desktop\\require.rb"
    deltoreCyclebin(filename)
