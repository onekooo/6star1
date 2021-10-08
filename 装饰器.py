
def check(func):
    # 代码读到@的时候就执行了，所以代码不要写在inner()函数外,此行应该被注释掉。
    print('登陆验证xxx')
    def inner():
        print('登陆验证')
        func()
    return inner



@check
def fss():
    print('发说说')


fss()
