

# .join() 字符串连接
print('_'.join('hello'))  # h_e_l_l_o
# .join()定义字符串列表
arr = ['1', '2', '3', '4', '5', '6', '7', '8']
print(''.join(arr))

# .replace(oldStr, newStr,count) 替换 count默认全选
# .split(subStr,count) 按subStr切割  subStr空白默认空白切割  count默认全选 return []
newStr = 'hello world world world world '
print(newStr.replace('w', ""))
print(newStr.replace('w', "", 1))
print(newStr.split('w'))
print(newStr.split())
print("****************")


# find rfind index rindex count 参数相同

my_str = 'hello world'
# .find(sub_str,start,end) 默认0.len（步长为正） not found return -1
# rfind right find
index = my_str.find('or')
print(index)
# index 与find用法相同 没有找到返回异常
# rindex right index
# print(my_str.index('a'))
print()
# count string 出现次数
print(my_str.count('o'))
print(my_str.count('or'))
