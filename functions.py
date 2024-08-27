def sum(num1, num2=5):
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2


print(sum(1))


def multiple_items(*args):
    print(args)
    for arg in args:
        print(arg)
        print(type(arg))
    print(type(args))


multiple_items("Hello", "World", "And", "Jupiter", 369)


def multi_keyvaluepairs_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_keyvaluepairs_items(first="Gerrel", last="Atanacio", age=31)


def add_one(num):
    if num >= 9:
        return num + 1
    total = num + 1
    print(total)
    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)
