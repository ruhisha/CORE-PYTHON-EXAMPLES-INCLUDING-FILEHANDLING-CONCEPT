try:
    f=open("sample.txt")
    s=f.read()
    print(s)
except FileNotFoundError as fe:
    print(fe)

print(".......................................")

try:
    f=open("file.txt")
    s1=f.read()
    print(s1)
except FileNotFoundError as fe:
    print(fe)