with open("sample.txt")as se:
    s=se.read()
    print(s)

print("..................................")

with open("sample.txt")as file:
    for x in file:
        print(x)
