# 获取数组中的一段，省去遍历
# 变量[start:end:step] not included end

my_str = 'hello world'

# 获取0-4
my_str1 = my_str[0:5]
print(my_str1)

# 获取0，2，4
my_str2 = my_str[0:5:2]
print(my_str2)

# 获取6-len
my_str3 = my_str[6:]
print(my_str3)

# 获取6
my_str4 = my_str[6]
print(my_str4)

# 0-5
my_str5 = my_str[:6]
print(my_str5)

# 获取All
my_str6 = my_str[:]
print(my_str6)

# step<0 逆序输出
my_str7 = my_str[4::-1]
print(my_str7)

# reverse the string
my_str8 = my_str[::-1]
print(my_str8)
