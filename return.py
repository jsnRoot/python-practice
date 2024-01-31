def callme(*args):
    for i in args:
        return i

sayName = callme("sachin")
print(sayName)