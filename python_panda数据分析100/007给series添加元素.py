import pandas as pd
grades={"语文":80,"数学":90,"英文":85,"计算机":100}
data = pd.Series(data = grades)

#data 是series类型，有一个append追加方法，生产一个新的对象，不是在原对象本身追加。
data = data.append(pd.Series(
    {
        "物理": 90,
        "化学": 88
    }
))

print(data)