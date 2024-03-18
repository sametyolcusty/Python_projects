list_methods = [method for method in dir(list) if not method.startswith("__")]
set_methods = [method for method in dir(set) if not method.startswith("__")]
string_methods = [method for method in dir(str) if not method.startswith("__")]
tuple_methods = [method for method in dir(tuple) if not method.startswith("__")]
dict_methods = [method for method in dir(dict) if not method.startswith("__")]

names = ["List Methods","Set Methods","String Methods","Tuple Method","Dict Method"]
headers = [list_methods,set_methods,string_methods,tuple_methods,dict_methods]
for name in names:
    print(name,end= "")
    print(" " * (30 - len(name)), end="")
max_len = 0
for header in headers:
    if len(header) > max_len:
        max_len = len(header)
for i in range(max_len):
    print()
    for header in headers:
        if i > len(header) - 1:
            print("-------", end="")
            print(" " * 23, end="")

        else:
            print(header[i], end="")
            print(" " * (30 - len(header[i])), end="")