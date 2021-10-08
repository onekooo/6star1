'''
使用pandas
把列表转成Series对象
并输入到命令后

'''
import pandas as pd
courses =["语文","数学","英语","计算机"]
data = pd.Series(data = courses)
print(data)