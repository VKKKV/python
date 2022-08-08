from operator import truediv
# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
import math
print(dir(math))


a = 234

# return two elements defaults for tuple
# no return value defaults to None
def f4():
    return 3,True
b=f4()
print(b)



# function can not directly modify the global variables
def f3():
    global a
    a = 123


print(a)
f3()
print(a)


def f1():
    print("F1")


# a,b are local variables局部变量
# the b=0 is defaults value for local variables
def f2(a, b=0):
    print(a+b)


print("this is a function test")
f1()
f2(1, 2)

print("this is a function test")


# help() view function documentation
help(print)
