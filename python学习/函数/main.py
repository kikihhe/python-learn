name = "asdf"


# 函数必须先定义后使用
def my_len(s):
    count = 0
    for i in s:
        count += 1
    return count


print(my_len(name))
