def fun1():
    print("function1")
    fun2()
def fun3():
    fun2()
    print("function3")
def fun4():
    print("function4")
    fun3()
def fun2():
    print("function2")
fun1()
fun2()
fun3()
fun4()
