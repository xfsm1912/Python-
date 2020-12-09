import sys

a = []

# 两次引用，一次来自a， 一次来自getrefcount

print(sys.getrefcount(a))


def func(a):
    # 四次引用，a，python的函数调用栈，函数参数，和getrefcount
    print(sys.getrefcount(a))

func(a)

# 两次引用，一次来自a，一次来自getrefcount, 函数func调用已经不存在
print(sys.getrefcount(a))

a = []
print(sys.getrefcount(a)) # 两次
b = a
print(sys.getrefcount(a)) # 三次
c = b
d = b
e = c
f = e
g = d

print(sys.getrefcount(a)) # 八次
