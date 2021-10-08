
'''
series -> dataframe
数据列名为：grade，输出到命令行
'''

import pandas as pd
grades={"语文":80,"数学":90,"英文":85,"计算机":100}
data = pd.Series(data = grades)

df = pd.DataFrame(data,columns=['grade'])
print(df)