def myParams(**myParams):
    if 'name' not in myParams:
        print("error")
    print("Hello", myParams['name'])

myParams(name="sachin",age=24, city="chilaw")

def printArgs(name, age):
    print(name)
    print(age)

args = {
    'name':"sachin",
    'age':24
}

printArgs(**args)