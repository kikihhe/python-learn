"""
@Project ：StudentManagerSystem
@File    ：managerSystem.py
@IDE     ：PyCharm
@Author  ：咋
@Date    ：2023/5/10
"""

# 初始图书
books = [['<<西游记>>', '吴承恩'], ['<<水浒传>>', '施耐庵'], ['<<三国演义>>', '罗贯中'], ['<<红楼梦>>', '曹雪芹']]
# 初始用户名/密码
users = [['admin', '123'], ['th', '456']]
flag = 0


#注册
def register():
    user = input('请输入用户名: ')
    password = input('请输入密码: ')
    # 输入用户名密码后将其加入users列表
    users.append([user, password])
    print('注册成功!')


# 登陆，判断输入的用户名、密码是否存在于users列表中，如果用户名、密码任意一项不在，打印错误信息:"用户名或密码错误!"
def login():
    f = 1
    while f:
        user = input('请输入用户名: ')
        password = input('请输入密码: ')
        if [user, password] in users:
            ui()
            f = 0
        else:
            print('用户名或密码错误!')


# 登陆后的界面
def ui():
    global flag
    flag = 1
    while flag:
        print('**********************')
        print('**********************')
        print('   欢迎登陆图书管理系统   ')
        print('*** 1.查看所有书籍 ***')
        print('*** 2.借书 ***')
        print('*** 3.还书 ***')
        print('*** 4.退出系统 ***')
        print('**********************')
        print('**********************')
        num = int(input('请输入你的操作: '))
        # 1: 查看所有书籍
        if num == 1:
            print('作者', '\t', '书籍')
            # 遍历books列表，打印所有信息
            for i in books:
                print(i[0], '\t', i[1])
        # 借书，只考虑书籍已存在的情况
        elif num == 2:
            book = input('请输入你要借的书名: ')
            author = input('请输入所要借的书的作者: ')
            if [book, author] in books:
                books.remove([book, author])
                print('出库成功!')
        elif num == 3:
            book = input('请输入你要还的书名: ')
            author = input('请输入所要还的书的作者: ')
            books.append([book, author])
            print('入库成功!')
        elif num == 4:
            exits()
        else:
            print('输入错误，请在输入!')


#离开系统
def exits():
    global flag
    flag = 0
    print('欢迎再次使用图书管理系统!')


#主界面
def main():
    global flag
    flag = 1
    # 死循环打印menu
    while flag:
        print('******************')
        print('******************')
        print(' 欢迎登陆图书管理系统 ')
        print('*** 1.register ***')
        print('*** 2.login    ***')
        print('*** 3.exits    ***')
        print('******************')
        print('******************')
        num = int(input('请输入操作数字:'))
        try:
            if num == 1:
                register()
            elif num == 2:
                login()
            elif num == 3:
                exits()
            else:
                print('输入错误，请重新输入！')
        except ValueError:
            print('输入错误，请重新输入！')


main()

