#第一题：
#for循环，99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}x{i}={j * i:<2}', end=' ')
    print()

#while循环，99乘法表
i = 1
while i <= 9:  # 行
    j = 1
    while j <= i:  # 列
        print(f'{j}x{i}={j * i:<2}', end=' ')
        j += 1
    print()
    i += 1
else:
    print('正常结束')

#第二题
#while循环打印1-12,排除6/10
n = 1
while n <=12:
    if n == 6 or n == 10:
        n += 1
        continue
    print(n)
    n += 1


#第2个方法while循环，break中断 排除6/1
n = 1
while True:
    if n == 6 or n == 10:
        n += 1
        continue
    print(n)
    n += 1
    if n == 13:
        break


# for循环打印1-12：排除6/1
for i in range(1,13):
    if i == 6 or i == 10:
        continue
    else:
        print(i)


#第三题：
#for循环计算：2-3+4-5+6-7+8-9...+100的和：
sum = 0
for n in range(2,101):
    if n % 2 == 1:
        sum -= n
    else:
        sum += n
print(sum)

#while循环计算：2-3+4-5+6-7+8-9...+100的和
sum = 0
n = 2
while n <=100:
    if n % 2 == 0:
        sum += n
        n += 1
    else:
        sum -= n
        n += 1
print(sum)

#第四题
#while循环任意数字累加到200
sum = 0
while sum <= 200:
    try:
        n = float(input('请输入一个数字：'))
        sum += float(n)
        print(f'和为{sum}')
        if sum > 200:
            print(f'累加和大于200,已退出。')
            break
    except ValueError:
        print('请输入数字。')