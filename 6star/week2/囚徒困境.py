a = input('A，你认罪吗?(认罪：y/不认罪:n)').strip()
b = input('B，你认罪吗?(认罪：y/不认罪:n)').strip()

if a == 'y' and b == 'y':
    print('A和B全部判罪10年。')
elif a == 'n' and b == 'y':
    print('A判罪20年，B判罪1年。')
elif a == 'y' and b == 'n':
    print('A判罪1年，B判罪20年。')
elif a == 'n' and b == 'n':
    print('A和B全部判罪3年。')
else:
    print('请正确输入y或n.')