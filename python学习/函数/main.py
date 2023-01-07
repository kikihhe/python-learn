name = "asdf"


# 函数必须先定义后使用
def my_len(s):
    count = 0
    for i in s:
        count += 1
    return count


def add(a, b):
    return a + b


print(my_len(name))
result = add(10, 20)
print(result)


# 函数返回值 : None
# 如果函数不使用return返回数据，默认返回None，表示: 返回了个无意义的数. 可以使用一个参数接收它，打印结果为None
def say_hi():
    1 + 1

result1 = say_hi()
print(result1)
