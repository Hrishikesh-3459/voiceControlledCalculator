s = "3.4 + 2.2 + 2"
for i in s.split():
    if i.isnumeric():
        print(f"{i} is numeric")
    if i.isdigit():
        print(f"{i} is digit")
    if i.isdecimal():
        print(f"{i} is decimal")
    try:
        print(f"{float(i)} is float")
    except:
        print("lol")