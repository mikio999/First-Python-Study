def myfunc(**kwargs):
    result = ""
    for i in kwargs.values():
        result += i
    return result
print(myfunc(a="Hi!", b="Mr.", c="Kim"))
