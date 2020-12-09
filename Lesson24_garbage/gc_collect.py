import gc
import os
import psutil


# 显示当前python程序占用的内存大小
def show_memory_info(hint):
    pid = os.getgid()
    p = psutil.Process()

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print(f'{hint} memory used: {memory} MB')


show_memory_info('initial')

a = [i for i in range(10000000)]

show_memory_info('after a created')

del a
gc.collect()

show_memory_info('finish')
print(a)




