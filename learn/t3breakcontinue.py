# for nested &break continue
from time import process_time_ns
from xml.etree.ElementInclude import include


for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print('@ ', end='')
    print()

print()

for i in range(5):
    for j in range(5):
        if j == 3:
            continue
        print('@ ', end='')
    print()

print()
for i in 'hello world':
    if i == 'a':
        print('include a')
        break
    else:
        print('not include a')

# 省去bool
print()
for i in 'hello world':
    if i == 'a':
        print('include a')
        break
# 不被break终止的时候会执行
else:
    print('not include a')

#连续输出
print('hello'*3)


#正负数下标
s="Hello"
#获取字符串长度
len(s)


