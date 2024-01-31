x = [12, 13, 14, 15, 16]

index =0


for item in x:
    y = x[index]
    print(y)
    index+=1

for item in enumerate(x):
    index, value = item
    print(index , value)

for item in range(0,10):
    print(type(item))
    if item == 5 : break