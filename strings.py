### this function will only return new string without afeecting the original string

name = "Rorger Moore"

print(name.lower())
print(name.upper())

print(name.find('M')) # it will search and give index if found, otherwise it will give -1
print(name.find('x')) # -1
print(name.find('ger')) #substring
print(name.replace("Moore", "Fedrer"))

# exists or not
print("F" in name)
print("e" in name)
print("Moore" in name)