"""
@Project ：StudentManagerSystem
@File    ：managerSystem.py
@IDE     ：PyCharm
@Author  ：j
@Date    ：2023/5/11

通讯录管理系统
实现的主要功能有:
能够循环接收客户端输入的功能编号，并根据编号选择对应的功能操作
用户输入“1”时，执行增加姓名和手机号码的操作
用户输入“2”时，执行删除姓名和手机号码的操作，根据用户输入姓名，删除对应手机号码
用户输入“3”时，执行修改手机号码的操作，根据用户输入姓名，修改对应手机号码
用户输入“4”时，执行显示全部姓名和手机号码的操作
用户输入“5”时，执行查询手机号码的操作，根据用户输入姓名，查找对应手机号码
用户输入“6”时，感谢用户使用，退出手机通讯录管理系统的程序
用户对于通讯录系统的操作是针对于相同内容的数据，而且联系人信息应该存在多条，所以应该存放在一个容器当中统一管理，
这里使用python自带数据结构中的列表进行存放，然后增删改查其实就是对于列表方法的调用。
"""

def addUser(contactlist):
    # 1.增加姓名和手机
    name = input("请输入姓名:>")
    # 判断姓名，在列表当中是否已经存储，如果存储，就提示用户不能存储，否则就存入
    flag = False  # 默认此人没存储过
    for index in range(len(contactlist)):
        if (contactlist[index][0] == name):
            print("此联系人已经存在，请重新输入！！")
            flag = True  # 设置此人已经存储
            break

    if not flag:
        phone = input("请输入手机号:>")
        singlelist = [name, phone]
        # 将一个人信息组成的列表，添加到总体的列表当中
        contactlist.append(singlelist)
        print("输入完成")


def deleteUser(contactlist):
    # 2.删除姓名
    name = input("请输入要删除的联系人:>")
    flag = False  # 默认这个人不存在
    # 遍历列表，查看这个列表当中是否包含此人
    for index in range(len(contactlist)):
        if contactlist[index][0] == name:
            # 说明此人存在
            del contactlist[index]
            flag = True
            print("删除成功")
            break
    if not flag:
        print("查无此人！")


def updateUser(contactlist):
    # 3.修改手机号码
    name = input("请输入要修改的联系人:>")
    flag = False  # 默认这个人不存在
    # 遍历列表，查看这个列表当中是否包含此人
    for index in range(len(contactlist)):
        if contactlist[index][0] == name:
            # 说明此人存在
            phone = input("请输入要修改的电话号码:>")
            contactlist[index][1] = phone
            flag = True
            print("修改成功")
            break

    if not flag:
        print("查无此人！")


def getAllUser(contactlist):
    # 4.查询所有用户
    print("-------------------")
    for i in contactlist:
        print("用户：\t%s\t\t%s" % (i[0], i[1]))
    print("-------------------")


def queryPhoneByName(contactlist):
    # 5.根据姓名查找手机号
    name = input("请输入要查询的联系人:>")
    flag = False  # 默认这个人不存在
    # 遍历列表，查看这个列表当中是否包含此人
    for index in range(len(contactlist)):
        if contactlist[index][0] == name:
            # 说明此人存在
            print("您要查找的手机号码是：%s" % (contactlist[index][1]))
            flag = True
            break
    if not flag:
        print("查无此人！")


def work(contactlist):
    while True:
        num = input("请根据规则继续输入:>")
        # 判断用户输入码是否在1，2，3，4，5，6当中
        if num not in ['1', '2', '3', '4', '5', '6']:
            print("输入有误，请重新输入")
        else:
            if num == '1':
                addUser(contactlist)
            elif num == '2':
                deleteUser(contactlist)
            elif num == '3':
                updateUser(contactlist)
            elif num == '4':
                getAllUser(contactlist)
            elif num == '5':
                queryPhoneByName(contactlist)
            elif num == '6':
                # 6.退出
                print("感谢使用")
                break


def main():
    # 因为可能存储多组数据，创建一个列表，目前列表没有元素，所以为空列表
    contactlist = []
    info = '''
    ====通讯录管理系统====
    1.增加姓名和手机
    2.删除姓名
    3.修改手机
    4.查询所有用户
    5.根据姓名查找手机号
    6.退出
    =====================
    '''
    print(info)
    work(contactlist)


if __name__ == "__main__":
    main()