import pandas as pd
#加载字典创建dataframe
df = pd.DataFrame(
    {
        "姓名":['张三','李四','王五','赵六'],
        "性别":['男','女','男','女'],
        "年龄":[18,19,20,21]
    }
)

print(df)