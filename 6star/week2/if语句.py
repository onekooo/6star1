#计算三个数字之和
#数字可能是整数和小数
sum = 0
n = 1
while n < 4:
    try:
        num = float(input(f'请输入第{n}数字，计算它们之和：'))
        sum = sum + num
        n += 1
    except ValueError:
        print('请输入一个数字。')

def my_sum(sum):
    return f'您输入的三个数的和是{sum}'

if sum > 100000:
    print(my_sum(sum),'忒大了')
elif sum > 10000:
    print(my_sum(sum),'挺大')
elif sum > 1000:
    print(my_sum(sum),'有点大')
elif sum > 100:
    print(my_sum(sum),'不算大')
elif sum > 10:
    print(my_sum(sum),'忒小了')
else:
    print(my_sum(sum),'不能再小了')
