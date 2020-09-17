# -*- coding: utf-8 -*-
import _thread
import time

def fun1():
    print("hello world %s" % time.ctime())
    
#多线程
def main():
    _thread.start_new_thread(fun1, ()) #无参数
    _thread.start_new_thread(fun1, ())
    time.sleep(2)
    print("over")

#程序成功在同一时刻运行两个函数
if __name__ == '__main__':
    main()
