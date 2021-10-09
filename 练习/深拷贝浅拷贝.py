import copy

#b = a: 赋值引用，a 和 b 都指向同一个对象。
#b = a.copy(): 浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。
#b = copy.deepcopy(a): 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。

print('浅拷贝:')
a = {1: [1,2,3]}
b = copy.copy(a)
print(a,b)
a[1].append(4)
print(a,b)

print('深拷贝:')
c = copy.deepcopy(a)
print(a,c)
a[1].append(5)
print(a,ck)