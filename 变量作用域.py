#L -> E -> G -> B

def test1():
    a = 1
    def test2():
        #修改外层的变量用nonlocal
        nonlocal a
        a = 10
        print(a)
    test2()
    print(a)
test1()