
'''
闭包函数有2个条件
1. 函数嵌套
2. 内部函数引用外网函数变量或参数
3. 外部函数返回内部函数
'''

# def waibu():
#     num = 10
#     def neibu():
#        print(num)
#     return neibu

#如果需要修改外部函数变量值需要使用nonlocal：
def waibu():
    num = 10
    def neibu():
        nonlocal num
        num = 100
        print(num)
    print(num)
    neibu()
    print(num)
    return neibu


result = waibu()
# result()


