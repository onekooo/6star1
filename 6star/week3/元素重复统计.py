'''
2. 数字重复统计:
（1）随机生成1000个整数；
（2）1000个数字生成的范围[20, 100]
（1000个数字都是属于20-100这个范围内）
（3）升序输出1000个数字中所有不同的数字及其每个数字重复出现的次数。
'''
import random
from collections import Counter

my_num  = []
for _ in range(0,1000):
    n = random.randint(20, 100)
    my_num.append(n)
# print(my_num)

#方法1:利用Counter函数
print(f'方法1：{len(my_num)}个数字')
# res = dict(sorted(dict(Counter(my_num)).items()))
res = Counter(my_num)
my_dict1 = dict(res)
print(sorted(my_dict1.items()))

#方法2：利用 列表count方法
print(f"方法2 {len(my_num)}个数字:")
s = set()
my_dict2 = {}
for n in my_num:
    if n not in s:
        s.add(n)
        my_dict2[n] = my_num.count(n)
print(sorted(res.items()))

#方法3：利用字典：如果列表元素在字典的keys里，那么字典value加1,否则等于1 效率低
print(f'方法3: {len(my_num)}个数字:')
my_dict3 = {}
for i in my_num:
    if i in my_dict3.keys():
        my_dict3[i] += 1
    else:
        my_dict3[i] = 1
print(sorted(my_dict3.items()))