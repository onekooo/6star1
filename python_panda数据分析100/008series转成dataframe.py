import pandas as pd
# courses =["语文","数学","英语","计算机"]
grades={"语文":80,"数学":90,"英文":85,"计算机":100}
data = pd.Series(data = grades)
print(data)
df = data.reset_index()
print(df)
df.columns = ["course",'grade']

print(df)