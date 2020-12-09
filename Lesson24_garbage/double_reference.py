# 显示当前python程序占用的内存大小
import gc
import os
import psutil


def show_memory_info(hint):
    pid = os.getgid()
    p = psutil.Process()

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print(f'{hint} memory used: {memory} MB')


def func():
    show_memory_info('initial')
    a = [i for i in range(1000000)]
    b = [i for i in range(1000000)]
    show_memory_info('after a, b created')
    a.append(b)
    b.append(a)


func()
gc.collect()
show_memory_info('finished')

