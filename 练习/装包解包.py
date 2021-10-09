#不定长参数
def my_sum(*args):
    #装包,打印一个元素，是一个整体
    print(args)
    #解包,打印两个数字，1，2
    print(*args)

def afun(a,b):
    print(a)
    print(b)


def my_sum1(**kwargs):
    #装包
    print(kwargs)
    #解包
    afun(**kwargs)

my_sum(1,2)

my_sum1(a=1,b=2)