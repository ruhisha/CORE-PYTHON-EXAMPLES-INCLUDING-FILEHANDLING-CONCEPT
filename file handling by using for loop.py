f=open("sample.txt","r")
for x in f:
    print(x)
f.close()

print("............................")

f=open("sample.txt","r")
s=f.readlines()
print(s)
print(len(s))