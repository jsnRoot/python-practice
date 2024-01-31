x = {
    "1":"sachin",
    "2":"nishalka",
    "3":"fernando"
}

print(x)

x["4"]="sandaru"

print(x)
print(x.keys())
print(x.values())
print(x.get(3, "no data"))

del x["2"]
print(x)

x.clear()
print(x)


y = {
    "a" : ["hello", "hi", "gm"],
    "b" : ["bye", "go home", "gn"]
}
y["a"].append("added by me")
print(y["a"])

