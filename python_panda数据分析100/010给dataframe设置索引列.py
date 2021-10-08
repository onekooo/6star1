import pandas as pd

data ={
        "姓名":['张三','李四','王五','赵六'],
        "性别":['男','女','男','女'],
        "年龄":[18,19,20,21]
    }

df = pd.DataFrame(data)

df.set_index('姓名',inplace=True)

print(df)