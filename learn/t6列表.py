
arr = [1, 2.3, True, 'abc']
arr2 = [1, 2, 38, 7, 64, 1]


# ！列表嵌套

# 逆置 reverse 修改原列表 | [::-1] 不修改源列表
arr2.reverse()
print(arr2)
arr4 = arr2[::-1]
print(arr4)


# .sort()要求列表中元素的数据类型一致，默认从小到大
# .sort(reverse=True)逆序，从大到小
# .sorted 区别不改变原列表，return新排序列表
arr3 = sorted(arr2)
print(arr3)

arr2.sort()
arr2.sort(reverse=True)
print(arr2)

# 列表删除 del(根据下标删除)
# pop(默认delete and return the last element也可根据下标)
print(arr.pop())
# remove(根据数值删除，无则报错)

# 列表的查询方法 index count
# in/not in(in is true,not is false )
b = True in arr  # true
c = False not in arr  # true
print(b)
print(c)


# 可直接对列表进行操作
# .append insert()
arr.append(True)
arr.insert(0, True)
arr.remove(True)

# extend列表末尾追加可迭代对象
arr.extend('hello')
arr.extend([1, 'hello', 2])

print(arr)

# 列表遍历
for i in arr[1:]:
    print(i)

print('-'*30)

print(arr)
print(arr[1:])
print(arr[:3])
print(len(arr))
# 与字符串区别：可以按下标修改数据

s = "hello world"
# s[1]="h"     TypeError: 'str' object does not support item assignment

arr[1] = 3.14
print(arr[1])  # 3.14
