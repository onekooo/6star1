# 本程序模拟展示商品/购买商品/装进购物车/清空购物车/计算总价。。。

goods = [['Iphone', 10888], ['MacPro', 14800], ["xiaomi10", 3999], ['Coffee', 32], ['book', 80], ['Nike Shoes', 899],['Nokia', 10000]]

# 准备一个字典，key：序号，value：商品名
sn_and_goods_dict = {sn: good for sn, good in enumerate(goods, 1)}
# 准备空购物车
shopping_cart = []


# 展示商品
def show_goods_list():
    print('\n' + '商品展示'.center(43, '#'))
    for sn, good_price in enumerate(goods, 1):
        print(f'序号：{sn:<2d}  商品名：{good_price[0]:^15s}  价格:{good_price[1]:>7d}')
    print('#' * 45, '\n')


print('欢迎光临！')

while True:
    # 展示商品
    show_goods_list()
    input_num = input(f'1-{len(goods)}：挑选商品\n  q：退出\n  s：查看购物车\n  c：清空购物车\n  a：计算总价\n请选择： ')

    if input_num == 'q':
        print('\n欢迎下次再来！')
        break
    #展示购物车
    elif input_num == 's':
        print(f'\n目前你的购物车里有物品: {shopping_cart}')
    #清空购物车
    elif input_num == 'c':
        shopping_cart.clear()
        print(f'\n已经清空购物车。')
    #计算购物车总额
    elif input_num == 'a':
        selected_good_amount = 0
        for g in shopping_cart:
            selected_good_amount += g[1]
        print(f'\n目前购物车总额为：{selected_good_amount}元')
    # 判读输入的字符是否只由数字组成。序号需要在商品范围内
    elif input_num.isdigit() and len(goods) >= int(input_num) > 0:
        selected_good = sn_and_goods_dict[int(input_num)]
        print(f'\n你选择了 <{selected_good[0]}>')
        shopping_cart.append(selected_good)
    else:
        print(f'\n您输入的商品不存在。')
