name = "sachin"
age = 25

message = "Hello {0}. You are {1} years old.".format(name, age)

message2 = f"Hello {name} and age is {age:05d}"
print(message)
print(message2)