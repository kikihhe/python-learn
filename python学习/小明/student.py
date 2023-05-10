
"""
@Project ：StudentManagerSystem
@File    ：student.py
@IDE     ：PyCharm
@Author  ：咋
@Date    ：2023/5/10
"""

# 学生类，属性: 姓名、性别、电话号
class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    # 调用__str__快速输入学生的信息
    def __str__(self):
        return f"{self.name},{self.gender},{self.tel}"