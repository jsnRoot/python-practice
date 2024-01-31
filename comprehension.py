def is_odd(number):
    return "odd" if number % 2 == 1 else "even"

a = [10, 11, 12, 13, 14, 15, 16, 17]

b = []
b = {  value : is_odd(value) for i,value in enumerate(a) if i % 2 ==0 }

print(b)