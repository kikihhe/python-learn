'''
注意：
1.要求输入的姓名默认全部为合理输入，并未对输入内容进行判断和过滤
2.默认打开的文件已经存在，并没对文件状态进行判断，而是以列表信息中是否存在该学生为依据
3.没有使用字典的任何操作
4.如果希望将所有学生信息保存在同一个txt文件中，只需将每个函数中file_name重新命名的部分注释掉
5.修改信息采用的方法是：将原内容删除，并重新写入新内容，这么做的原因是电脑要没电了，这个可以作为自己的测试板块，重新设计编写
6.实验步骤的最后一步 不知道是什么目的，并所以没有这样做
7.因为都是采用列表来判断学生内容，所以文件保存成功后重新运行程序列表清空，即不可再查询到信息
8.打印所有信息可以采取文件夹下多文件读取的方法，遍历该目录下的所有txt文件，读出内容并打印，请自行编写


新增注意：
1.修改文件内容时，如果将姓名一同修改，则会出现文件名与文件内容中的姓名不同的情况
2.修改文件内容时，如果将该姓名修改为另一个已经出现过的姓名，在列表中将会出现重名情况
3.先没有处理重名情况的操作
4.同名情况下，如果修改该名字的信息，则将修改第一次出现该名称的位置的信息
5.因此，如果错误1和错误2同时发生，文件就会，嗯...串了，就乱套了

'''




Student = []
path = "D:\\"  #文件保存路径 默认为空即保存在当前文件夹下 建议新建文件夹并修改路径
file_name = path + "student.txt" #文件默认保存位置

#显示命令
def print_message():
    print("**************************************")
    print("     **1.添加学生信息")
    print("     **2.删除学生信息")
    print("     **3.修改学生信息")
    print("     **4.查找学生信息")
    print("     **5.查看所有信息")
    print("     **6.查看操作菜单")




#添加信息
def add():
        print("请输入需要添加到姓名、手机号，以空格隔开：")
        #列表
        A = input().split(" ")
        temp_str = ""
        for i in A:
            temp_str += i+"  "
        if temp_str != '/n': #防止错误输入
             Student.append(A)  #加入列表
             file_name = path+A[0] +".txt"
             print(temp_str, file=open(file_name, 'w'))  #创建文件，并写入文件  如果存在同名文件，则原内容会被覆盖
        #字典
        # A = input().split(" ")
        # Name.append(A[0])
        # d[A[0]] = A[1]
        # print("添加成功")
        # save(A[0])  # 更新学生信息

#删除信息
def delete():
    print("请输入需要删除的姓名：")
    name = input()
    #字典删除
    # del d[name]
    # Name.remove(name)
    #从文件中删除学生信息
    exist = 0
    for i in range(len(Student)):
        #存在该学生
        if Student[i].count(name) > 0:
            if name == Student[i][0]:
                file_name = path + name + ".txt"
                #删除列表中的信息
                Student.pop(i)
                #删除文件中的信息
                lines = [l for l in open(file_name, "r") if l.find(name, 0, len(name)) != 0] #暂时的删除方式
                fd = open(file_name, "w")                                                    #如： 要删除’张三‘，但‘张三四’也会被删除
                fd.writelines(lines)
                fd.close()
                print("删除成功")
                exist = 1  #判断学生是否存在的标签
                break
        else :
            exist = 0
    if exist == 0:
         print("未找到该学生的信息！")


def delete_2(name,f_n):
      # 从列表里删除该学生
        for i in range(len(Student)):
            # 存在该学生
            if Student[i].count(name) > 0:
                if name == Student[i][0]:
                    del Student[i]
                    break

        #从文件中删除学生信息
        lines = [l for l in open(f_n, "r") if l.find(name, 0, len(name)) != 0]
        fd = open(f_n, "w")
        fd.writelines(lines)
        fd.close()




#查询信息
def search():
    print("请输入需要查询的姓名：")
    name  = input()
    #字典查询
    #print("查询结果：",name,d[name])
    exist = 0
    for i in range(len(Student)):
        #存在该学生 这一步判断有点多余 但是为了简化打印未找到的结果还是这样做了
        if Student[i].count(name) > 0:
            if name == Student[i][0]:
                print("查询结果: ")
                for temp in Student[i]:
                    print(temp,end=" ")
                print()
                exist = 1  # 判断学生是否存在的标签
                break
        else:
                exist = 0
    if exist == 0:
                print("未找到该学生的信息！")

#更改文件信息
def change_file():
    print("输入需要修改信息的学生姓名：")
    name = input()
    exist = 0
    for i in range(len(Student)):
        #存在该学生
        if Student[i].count(name) > 0:
            if name == Student[i][0]:
                # 找到了该学生
                # 下面进行修改信息的操作
                file_name = path + name + ".txt"
                print("输入修改后该学生的所有信息：")
                A = input().split(" ")
                temp_str = ""
                for i in A:
                    temp_str += i + "  "
                if temp_str != '/n':  # 防止错误输入
                    Student.append(A)  # 加入列表
                    delete_2(name,file_name) # 先删除该信息

                    print(temp_str, file=open(file_name, 'a'))  # 创建文件，并重新写入文件
                print("修改成功")
                exist = 1  # 判断学生是否存在的标签
                break
        else:
                exist = 0
    if exist == 0:
                print("未找到该学生的信息！")


#显示信息
def printf():
    print("所有信息如下：")
    for i in Student:
        for j in i:
            print(j,end=" ")
        print()





