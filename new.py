import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106], 
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"], 
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"], 
    "Salary": [50000, 45000, 60000, 55000,48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}
df = pd.DataFrame(data)
print(df["Salary"])
df["Marks"]=[98,99,100,89,94,96]
df["Marks"]=df["SalARY"]/2

df.drop("Emp_ID",axis=1,inplace= True)
print(df)

print(df.iloc[1])
print(df.loc[1])
print(df.iloc[0:3])
print(df.loc[0:3])

df1=df.iloc[0:2,[0,1]]
print(df1)