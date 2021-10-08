'''
用numpy创建series
使用numpy和pandas配合完成
类型：float
数值：10-90，每两个数字间隔10
'''

import pandas as pd
import numpy as np

s = pd.Series(
    np.arange(10,100,10),
    index = np.arange(101,110),
    dtype = 'float'
)

print(s)