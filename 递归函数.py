#确定的直接返回,不确定的继续分解
#求一个数的阶乘
'''
#传递与回归
5 * jiecheng(4)
    4 * jiecheng(3)
        3 * jiecheng(2)
            2 * jiecheng(1)
                1
'''
def jiesheng(n):
    if n == 1:
        return 1
    return n * jiesheng(n-1)

print(jiesheng(4))