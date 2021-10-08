
#初始化字母、特殊字符、数字
import math
import random

alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
special = '!@#$%&*^_+=()'

pass_len = int(input('Enter Password Lenth: '))

# 50-30-20
#字母占密码长度的1/2
alpha_len = pass_len // 2
#数字占密码长度的1/3
num_len = math.ceil(pass_len*30/100)
#特殊字符占密码长度的1/5
special_len = pass_len - num_len - alpha_len

password = []

def generate_pass(length,array,is_alpha = False):
    '''
    生成密码函数。
    length:密码长度，
    array: 组成密码数组,参数是否使用字母
    is_alpha: 是否使用字母
    '''
    for i in range(length):
        #随机生成一个数组下表
        index = random.randint(0,len(array)-1)
        #根据下班取出一个字符
        character = array[index]
        #如果使用字母
        if is_alpha:
            case = random.randint(0,1)
            if case == 1:
                # 如果case 为1 那么把当前循环的字符变成大写
                character = character.upper()
        #将本次循环生成的字符追加到密码中。
        password.append(character)
#生成字母组成部分
generate_pass(alpha_len,alpha,True)
#生成数字组成部分
generate_pass(num_len,num)
#生成特殊字符组成部分
generate_pass(special_len,special)

#再次将生成的随机串打算
random.shuffle(password)
gen_password = ''

for i in password:
    gen_password += str(i)

print(gen_password)

# print(help(generate_pass))