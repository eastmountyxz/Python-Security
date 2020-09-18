import telnetlib
import threading
import queue

#IP端口开发检测
def get_ip_status(ip):
    server = telnetlib.Telnet()
    for port in range(20,10000):
        try:
            server.open(ip,port)
            print('{0} port {1} is open'.format(ip, port))
        except Exception as err:
            #print('{0} port {1} is not open'.format(ip,port))
            pass
        finally:
            server.close()
 
def check_open(q):
    try:
        while True:
            ip = q.get_nowait()
            get_ip_status(ip)
    except queue.Empty as e:
        pass

#主函数
if __name__ == '__main__':
    host = ['210.40.81.16']     #模拟多IP地址
    q = queue.Queue()
    for ip in host:
        q.put(ip)
    threads = []
    for i in range(10):
        t = threading.Thread(target=check_open,args=(q,))
        t.start()
        threads.append(t)
 
    for t in threads:
        t.join()
