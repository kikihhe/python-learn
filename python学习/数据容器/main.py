# python中有以下几种数据容器:
# list(列表) name_list = [item1, item2, item3...]
# tuple(元组)
# str(字符串)
# set(集合)
# dict(字典)


# list--------------------------------------------------------------------------------------
# 列表中的元素类型可以是任何类型,不受限制。使用 参数名[下标] 来访问特定下标的元素。
# 直接输出列表: [元素1, 元素2, 元素3...]
# 列表的长度声明后不可变，除非重新申请内存或者调用内置方法
# 列表下标可以是负数，代表倒序，例如 -1代表倒数第一个元素
name1 = '小王'
name2 = '小刘'
name3 = '小何'
name4 = '小红'
name_list = [name1, name2, name3, name4]
count = 0
for item in name_list:
    print(f"item{count}: {item}")
    count += 1

name_list[1] = 1
print(name_list[1])

print(name_list)
# 列表中也可以有列表，
age_list = [1, 2, 3, 4]
name_list = [name1, name2, name3, name4, age_list]

print(name_list[4][2])
# list.insert(index, value) 向index位置插入一个值，其他值向后移动
name_list.insert(1, '小刚')
print(name_list)
