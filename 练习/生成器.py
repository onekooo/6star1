#使用小括号创造一个生成器

#列表推导式
# l = [i for i in range(1000000) if i % 2 == 0]
# print(l)

#使用小括号
scq = (i for i in range(1000000) if i % 2 == 0)
# print(next(scq))
# print(next(scq))
# print(next(scq))
# print(next(scq))
# print(next(scq))

print(scq)
for i in scq:
    print(i,end=' ')