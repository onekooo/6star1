name = 'maiya'
passwd = '123'
username = input('请输入用户名：')
password = input('请输入密码：')

if name == username.strip() and passwd == password:
    print('登陆成功')
else:
    print('登陆失败')
