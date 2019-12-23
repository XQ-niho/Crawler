# coding=utf-8

#线程停止

import threading
import time

#线程终止变量
isrunning = True

def thread_body():
    while isrunning:
        # 线程开始工作
        # TODO
        print('下载中...')
        time.sleep(5)
    print('执行完成！')

def main():
    t1 = threading.Thread(target=thread_body, name='ThreadA')
    t1.start()
    # 从键盘输入停止指令 exit
    command = input('请输入停止指令：')
    if command == 'exit':
        global isrunning
        isrunning = False

if __name__ == '__main__':
    main()
