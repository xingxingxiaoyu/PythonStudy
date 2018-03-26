def sum(n):
    result = 0
    for i in range(n):
        result += i
    return result


print(sum(10))


def sortList(list, isDesc=False):
    for i in range(len(list)):
        for j in range(1, len(list) - i):
            flag = list[j] < list[j - 1]
            if (isDesc):
                flag = not flag
            if (flag):
                list[j], list[j - 1] = list[j - 1], list[j]
    return list


L = sortList([12, 32, 13, 123, 76, 453, 23, 96])
print(L)
L = sortList([12, 32, 13, 123, 76, 453, 23, 96], True)
print(L)

i = 10


def f(a=i):
    print(a)


i = 20
f()


def f(a, L=[]):
    L.append(a)
    print(L)


f(1)
f(2)
f(3)


def f(a, s=""):
    s = s + str(a)
    print(s)


f(1)
f(2)
f(3)


def sum(*args):
    print(type(args))
    result = 0
    for i in args:
        result += i
    return result


print(sum(1, 2, 3))


def person(**kwargs):
    print(type(kwargs))
    print(kwargs)


person(name='Jack', age=23)


def person(*, name, age):
    print("name:", name, "age:", age)


person(name='Jack', age=23)


def person(*args, name, age):
    print(args, "name:", name, "age:", age)


person(1, 4, 5, age=23, name='Jack')


def person(*, name="Jack", age):
    print("name:", name, "age:", age)


person(age=23)


def person(name, age=0, *args, city="北京", address, **kwargs):
    print("name:", name, "age:", age, "args:", args, "city:", city, "address:", address, "kwargs:", kwargs)


person("Jack", 12, 32, 34, address="西二旗", sex="男", hobby="篮球")


def f(age: int, name: str = "jack") -> str:
    print(f.__annotations__)
    print(age, name)
    return name

print(f("10"))


def f():
    "用于测试文档的函数"
    print(f.__doc__)
    pass

f()