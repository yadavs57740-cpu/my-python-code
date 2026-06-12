import pandas as pd
d={
   "name":["vishal","virat","vineet"],
   "salary":[100,200,300]
}
df=pd.DataFrame(data=d)
print(df.loc[2,"name"])
print(df.iloc[2,0])

# get single row data using iloc
#print(df.iloc[1])

# get single row using loc
#print(df.loc[1])

# get multi rows using iloc
#print(df.iloc[0:3])

# get multi rows using loc
#print(df.loc[0:3])

# sub data get using iloc
df1=df.iloc[0:2,[0]] # rows -> 0,1 and cols -> 0 | name
df1

# sub data get using loc
df1=df.loc[0:2,[0]] # rows -> 0,1 and cols -> 0 | name
df1

import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106], 
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"], 
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"], 
    "Salary": [50000, 45000, 60000, 55000,48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}
df = pd.DataFrame (data)
print(df)
