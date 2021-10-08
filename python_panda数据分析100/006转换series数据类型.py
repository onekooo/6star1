import  pandas as pd

'''
series转换数据类型

str -> int
'''

s =pd.Series(
    data = ['001','002','003','004'],
    index= list('abcd')
)
print(s)
s = s.astype(int) #int是一个数据类型
print(s)
s = s.map(float) # 这里float是个函数
print(s)