from imp import source_from_cache


arr = [1,2.3,True,'abc']

# 列表遍历
for i in arr[1:]:
    print(i)

print('-'*30)

print(arr)
print(arr[1:])
print(arr[:3])
print(len(arr))
# 与字符串区别：可以按下标修改数据

s="hello world"
# s[1]="h"     TypeError: 'str' object does not support item assignment

arr[1]=3.14
print(arr[1]) # 3.14

