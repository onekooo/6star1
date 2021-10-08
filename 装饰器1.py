def getzsq(char):
    def zhuangshiqi_line(func):
        def inner(*args,**kwargs):
            print(char * 20)
            res = func(*args,**kwargs)
            return res
        return inner
    return zhuangshiqi_line

@getzsq('&*')
def print_content(n1,n2,n3,n4=666):
    print('越努力，越幸运。',n1,n2,n3,n4)
    res =  n1 + n2 + n3 + n4
    return  res


res = print_content(10,20,30)
print(res)