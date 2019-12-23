# coding=utf-8

# 线程管理
import threading
import time

#共享变量
value = 0

#线程体函数
def thread_body():
    global value
    #当前线程对象、
    print('ThreadA 开始...')
    for n in range(2):
        print('ThreadA 执行...')
        value += 1
        #线程休眠
        time.sleep(1)
    print('ThreadA 结束...')

def main():
    print('主线程开始...')
    t1 = threading.Thread(target=thread_body, name='ThreadA')
    t1.start()
    #主线程被阻塞，等待t1线程结束
    t1.join()
    print('value = {0}'.format(value))
    print('主线程结束...')

if __name__ == '__main__':
    main()