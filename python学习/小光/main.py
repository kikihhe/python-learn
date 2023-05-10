import manage

print("**************************************")
print("    欢迎来到学生信息管理系统")
manage.print_message() #打印命令指令
print("**************************************")
while(True):

    print("请输入需要执行的操作(输入’q‘退出程序)：")
    choice = input()
    if choice == '1':
        manage.add()   #增
    if choice == '2':
       manage.delete() #删
    if choice == '3':
       manage.change_file()  #改
    if choice == '4':
       manage.search()  #查
    if choice == '5':
       manage.printf()  #打印
    if choice == '6':
        manage.print_message()  # 打印命令指令
    if choice == 'q':
        print("退出！")
        break


