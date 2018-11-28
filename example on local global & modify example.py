a=100
c=500
def fun1():
    global a
    a=30
    print(a)
    fun2()
    print(a)
def fun2():
    print(a)
    b=20
    print(b)
    print(a+b)
def fun3():
    c=50
    print(c)
    print(a+c)
print(a)
print(c)
fun1()
fun2()
fun3()
print(c)