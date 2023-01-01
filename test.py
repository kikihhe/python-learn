# money = 100
# a = 1
# b = 1

# # money_type = type(money)
# # print(money_type)
# print(isinstance(money, int))
#
# a = "12.1"
# b = float(a)
# print(b)
# print(type(b))

# print("请输入:")
# money = input()
# print(f"输入的值为: {money}")
# print(2 > 6)

# name = input("请输入用户名:")
# if name == "小明":
#     if input("请输入密码:") == "123456":
#         print("登陆成功!")
#     else:
#         print("密码错误")
# else:
#     print("用户名错误!!")
# i = 10
# while i < 30:
#     print(i)
#     i += 1

# money = input("请输入你的工资:")
# money = int(money)
# if money <= 3000:
#     print("给老板当牛做马")
# elif 3000 < money < 7000:
#     print("还行")
# else:
#     print("公司是我家")
#
# sum = 0
# i = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)

# 输入一个字符串，统计其中a的数量
# count = 0
# name = input()
# for i in name:
#     if i == 'a':
#         count += 1
# print(count)


# 统计1-1000中有多少个素数

for i in range(2, 1000):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
    if flag:
        print(i)

