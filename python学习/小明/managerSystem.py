
"""
@Project ：StudentManagerSystem
@File    ：managerSystem.py
@IDE     ：PyCharm
@Author  ：咋
@Date    ：2023/5/10

此项目是基于Python的学生管理系统，提供的主要功能:
1.添加学员
2.删除学员
3.修改学员信息
4.查询学员信息
5.显示所有学员信息
6.保存学员信息
7.退出系统
用户添加学生后存入本文件夹路径的student.data中，下次将其加载进来。不提供自动保存功能，清退出前手动保存(功能7)以避免数据丢失
学生信息使用student类存储，student使用列表存储。
对于学生的任何操作都基于此列表进行(遍历增删改查)
"""
from student import *

# 学生管理类
class StudentManagement(object):
    # 列表存放学生信息
    def __init__(self):
        self.student_list = []
    # run方法，根据用户的输入确定使用哪一个功能
    def run(self):
        # 加载文件中存档的所有学生
        self.load_student()
        # 死循环展示菜单
        while True:
            self.show_menu()
            menu_num = int(input("请输入您需要的功能序号："))
            # 1: 新增学生
            if menu_num == 1:
                self.add_student()
            # 2: 删除学生
            elif menu_num == 2:
                self.del_student()
            # 3: 更改学生
            elif menu_num == 3:
                self.modify_student()
            # 4: 查询学生
            elif menu_num == 4:
                self.search_student()
            # 5: 展示所有学生
            elif menu_num == 5:
                self.show_student()
            # 6: 保存
            elif menu_num == 6:
                self.save_student()
            # 7: 退出系统
            elif menu_num == 7:
                break
            # 如果输入其他的数字，提示错误让用户重新输入
            else:
                print("您输入的序号有误，请重新输入！")

    # 菜单
    @staticmethod
    def show_menu():
        print("请选择如下功能：")
        print("1.添加学员")
        print("2.删除学员")
        print("3.修改学员信息")
        print("4.查询学员信息")
        print("5.显示所有学员信息")
        print("6.保存学员信息")
        print("7.退出系统")

    def add_student(self):
        name = input("请输入学员的姓名：")
        gender = input("请输入学员的性别：")
        tel = input("请输入学员的手机号")
        # 用户输入后将学生信息存入list
        student = Student(name, gender, tel)
        self.student_list.append(student)

    def del_student(self):
        del_name = input("请输入要删除的学员姓名：")
        # 遍历列表，找到就删除，找不到就打印、退出
        for i in self.student_list:
            # 按照姓名查询
            if i.name == del_name:
                self.student_list.remove(i)
                break
            else:
                print("查无此人！")
            print(self.student_list)

    def modify_student(self):
        # 原理是先查找，再修改，没找到就打印错误信息。
        modify_name = input("请输入学员姓名：")
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input("请输入更改之后的学员姓名：")
                i.gender = input("请输入更改之后的学员性别：")
                i.tel = input("请输入更改之后的学员手机号：")
                print(f"修改该学员信息成功，姓名：{i.name},性别：{i.gender},手机号：{i.tel}")
                break
        else:
            print("查无此人！")

    def search_student(self):
        # 根据姓名查找，没找到就打印错误信息，找到就打印学生信息
        # 不支持一次查找多个人，(学生不能重名)
        search_name = input("请输入您要查找的学员的姓名：")
        for i in self.student_list:
            if i.name == search_name:
                print(f"姓名：{i.name},性别：{i.gender},手机号：{i.tel}")
                break
            else:
                print("查无此人！")

    # 遍历列表展示所有学生的信息
    def show_student(self):
        print("姓名\t性别\t手机号")
        for i in self.student_list:
            print(f"{i.name}\t{i.gender}\t{i.tel}")
    # 将列表中的学生存入文件中
    def save_student(self):
        f = open("student.data", "w")
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        f.write(str(new_list))
        f.close()

    # 将之前存入文件的学生信息读出
    def load_student(self):
        try:
            f = open("student.data", "r")
        except:
            f = open("student.data", "w")
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i["name"], i["gender"], i["tel"]) for i in new_list]
        finally:
            f.close()
