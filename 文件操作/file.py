import collections.abc as collections
import os

# f = open('a.txt', 'r')
# print(type(f))
# 判断是否是迭代器，迭代器的好处：动态加载数据，而不是一次性全部加载，节省资源。
# print(isinstance(f, collections.Iterable))
# print(f.readlines())

#判断是否可以写
# if f.writable():
#判断是否可以读
# if f.readable():
#     for i in f.readlines():
#         for i in f:
#         print(f.tell())
        # print(i, end='')
#
# f.close()
# os.rename('b.txt','a.txt')
#按照目录树改名,two目录如果不存在，会把前边对应的one目录改为two
# os.renames('one/one.txt','two/two.txt')

# os.rename('aaaa')
#删除空目录
# os.rmdir('one/one2')

#递归删除,路径全部删除，如果不存在会报错。
# os.removedirs('one/one2')

#创建目录，不能创建多级目录，已存在，会报错。
os.mkdir('three')