#列表前面加星号作用是将列表解开成两个独立的参数，传入函数: 不定长参数和关键字参数
#字典前面加1个星号，是将字典key解开成独立的元素作为形参。
#字典前面加2个星号，是将字典value解开成独立的元素作为形参。

my_list = [1,2,3]
my_dict = {'name':'ty','age':18}
my_tuple = (4,5,6)

#一个型号+列表，相当于解包
print(*my_list)

#一个型号+元组，相当于解包,不支持两个星号
print(*my_tuple)

#一个型号+字典，返回字典key
print(*my_dict)

##两个型号+字典返回一个新的字典
print(id({**my_dict}))
print(type({**my_dict}))
print(id(my_dict))