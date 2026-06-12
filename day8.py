import pandas as pd
d = {
"name":["vishal","virat","vineet"], # 3 rows
"salary":[100,200,300] # 3 rows
}
df = pd.DataFrame(data=d)
# add column
# df["marks"] = [10,20,30]
df["marks"] = df["salary"] / 2
df["increment"]=df["salary"]+ (df["salary"]/10)
# column name change
df.rename(columns={"increment":"salary_increment"},inplace=True)
df