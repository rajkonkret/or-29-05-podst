# funkcja zagnieżdzona

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # tylko zwrócenie funkcji, czyli adresu funkcji, bez jej wykonania


xFun = fun1()  # To jest fun1

print(xFun)  # <function fun1.<locals>.fun2 at 0x000001FF97977060>
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2
