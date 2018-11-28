def fun3():
    a="hai"
    b="hello"
    return(a+b)
print(fun3())

print("...................................")

def add():
    no1=10
    no2=20
    return(no1+no2)
res=add()
print(res)

print("...................................")
def calc():
    no1=10
    no2=2
    a=no1+no2
    b=no1-no2
    c=no1*no2
    d=no1/no2
    return a,b,c,d
res=calc()
print(res)
print(type(res))