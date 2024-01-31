def callMe(upperbound):
    for i in range(0, upperbound):
        if(i % 2 == 0):
            yield i

x = callMe(100)

for i in x:
    print(i)