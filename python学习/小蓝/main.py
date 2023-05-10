import re
import os

info = []
boys = []
girls = []


# 定义功能界面函数
def info_print():
    print('----------------请选择 功能------------')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员信息')
    print('5.显示/打印所有学员（txt）')
    print('6.删除txt文件')
    print('0.退出系统')
    print('-------------------------------------')


# 定义添加学员信息的函数
def add_info():
    # 1.接收用户输入学员信息
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_sex = input('请输入性别：（男或女）')
    new_tel = input('请输入手机号：')
    # 声明info是全局变量
    global info
    # 2.检测用户输入的姓名是否存在，存在则报错提示
    for i in info:
        if new_name == i['name']:
            print('用户已存在')
            return

    # 3.如果用户输入的姓名不存在，则添加该学员信息
    info_dict = {'id': new_id, 'name': new_name, 'sex': new_sex, 'tel': new_tel}
    # 4.将用户输入的数据追加到字典
    # 5.将这个学员的字典数据追加到列表
    info.append(info_dict)


# 删除学员功能函数
def del_info():
    # 1.用户输入要输出的学员姓名
    del_name = input('请输入要删除的学员的姓名：')
    global info
    # 2.判断学员是否存在，存在则删除，否则报错提示
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在')
    print(info)


# 修改函数
def modify_info():
    # 1.用户输入要修改的学员的姓名
    modify_name = input('请输入要修改的学员的姓名：')
    global info
    # 2.判断学员是否存在：存在则修改，否则报错
    for i in info:
        if modify_name == i['name']:
            i['name'] = input('请输入新的姓名')
            i['id'] = input('请输入新的学号')
            i['sex'] = input('请输入性别')
            i['tel'] = input('请输入新的手机号：')
            break
    else:
        print('该学员不存在')
    print(info)


# 查询学员
def search_info():
    # 1.输入要查找的学员姓名：
    search_name = input('请输入要查找的学员姓名：')
    global info
    # 2.判断学员是否存在：是则显示该生信息，否则报错提示
    for i in info:
        if search_name == i['name']:
            print('查找到的学员信息如下：-------------')
            print(f"该学员的学号是{i['id']},姓名是{i['name']},性别为：{i['sex']},手机号是{i['tel']}")
            break
    else:
        print('查无此人......')


# 模糊查找
def fuzzy_finder(key, data):
    suggestions = []
    pattern = '.*%s.*' % key  # 正则表达式
    regex = re.compile(pattern)
    for item in data:
        match = regex.search(item['name'])
        if match:
            suggestions.append(item)
    return suggestions


# 统计性别
def sex_ratio():
    global info, boys, girls
    for i in info:
        if i['sex'] == '女':
            girls.append(i)
        elif i['sex'] == '男':
            boys.append(i)
    print(f'男生人数为：{len(boys)},女生人数为：{len(girls)}')


# 显示所有学员信息
def print_all():
    print("1.控制台显示\n2.打印到为txt文件（可供下载）")
    myFind = int(input("输入操作代码："))
    if myFind == 1:
        print('学号\t姓名\t性别\t手机号')
        for i in info:
            print(f"该学员的学号是{i['id']},姓名是{i['name']},性别为：{i['sex']},手机号是{i['tel']}")
    elif myFind == 2:
        create_file()
    else:
        print("输入有误")


def create_file():
    file = open("C:\\Users\\ASUS\\Desktop\\myTxt.txt", 'w', encoding="UTF-8")  # 写入内容
    file.write(str(info))
    file.close()


def delete_file():
    os.unlink("C:\\Users\\ASUS\\Desktop\\myTxt.txt")
    print("myTxt.txt已被删除")


while True:
    # 1.显示功能界面
    info_print()
    # 2.用户输入功能序号
    user_num = int(input('请输入功能序号：'))
    # 3.按照用户输入的功能序号，执行不同的功能（函数）
    if user_num == 1:
        add_info()
    elif user_num == 2:
        del_info()
    elif user_num == 3:
        modify_info()
    elif user_num == 4:
        print('请选择查找方式：\n1.精准查找\n2.模糊查找\n3.统计男女\n0.退出')
        myFind = int(input())
        if myFind == 1:
            search_info()
        elif myFind == 2:
            findName = input('请输入要查找的学员姓名：')
            result = fuzzy_finder(findName, info)
            print(result)
        elif myFind == 3:
            sex_ratio()
        elif myFind == 0:
            print('返回主菜单')
            continue
        else:
            print('输入有误，已返回主菜单')
            continue
    elif user_num == 5:
        print_all()
    elif myFind == 6:
        delete_file()
    elif user_num == 0:
        exit_flag = input('确定要退出吗？ yes or no')
        if exit_flag == 'yes':
            print('已退出程序')
            break
        elif exit_flag == 'no':
            print('返回主菜单')
            continue
        else:
            print('输入有误，已返回主菜单')
            continue
    else:
        print('输入的功能序号有误')
        continue