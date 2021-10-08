'''
使用pandas将Series转换成List
将List输出到命令行
'''

import pandas as pd
grades={"语文":80,"数学":90,"英文":85,"计算机":100}
data = pd.Series(data = grades)

numbers = data.tolist()

print(numbers)