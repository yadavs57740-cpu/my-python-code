# day 13
# pandas

#dict
import pandas as pd
dict = {"name":["dheeraj","kunal","yash","praveen","anjali"],
        "age":[20,21,22,23,24],
        "salary":[{"In-hand":"15000","ctc":"1.2lpa"},{"In-hand":"20000","ctc":"2.2lpa"},
                  {"In-hand":"25000","ctc":"3.2lpa"},{"In-hand":"30000","ctc":"3.2lpa"},
                  {"In-hand":"40000","ctc":"4.2lpa"}
                  ]  
        }
df = pd.DataFrame(dict)
print(df)


#csv
# import pandas as pd
# df=pd.read_csv("file1.csv")
# print(df)

# #json
# import pandas as pd
# df=pd.read_json("file1.json")
# print(df)

#excel
import pandas as pd
df=pd.read_excel("file1.xlsx")
print(df)

#excel to json
df.to_json("file2.json")
df.to_csv("file2.csv")


# day 14
# create DataFrame

# import package pandas
# 1d -> method Series

import pandas as pd
#example 1
l = [10,20,30]
df = pd.Series(data=l)
print(df)
print(df[0])

#example 2
d = {"name":"kunal","age":"21","roll-no":123}
df = pd.Series(data=d,index=["name","age","roll-no"])
print(df)

# suggestion
# help(pd.Series)
# pd.Series??


import pandas as pd
d = {
    "name":["kunal","dheeraj","anjali","praveen","yash","danish"],
    "roll-no":[12,13,14,15,16,17]
}
df = pd.DataFrame(data=d)
print(df)
     
# csv file import from github
import pandas as pd
url = "https://github.com/yadavs57740-cpu/my-python-code/blob/main/file3.csv"
df = pd.read_csv(url)
df


# json file import from github
import pandas as pd
url = "https://github.com/yadavs57740-cpu/my-python-code/blob/main/file3.json"
df = pd.read_json(url)
df.rename(columns={"marks":"student_marks"},inplace=True)
df


# Basic Dataframe Understanding
# head() , tail() , shape , info() , rename , describe()-> count,mean,std,min,max

# head()
# csv file import from github
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df
# head  -> starting 5 rows
df.head(2)
# head -> 2 rows data
df.head(-3)
# head -> negative number


# tail()
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df
# tail used for get last 5 rows data
df.tail(2)
# tail in negative
df.tail(-1)


# shape
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df
df.shape # rows -> 5 and cols -> 3


# info()
import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
# df["salary"] = [100,200,300,np.nan,500]
df.info()
     

#rename
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df.rename(columns={"name":"student_name","marks":"salary"},inplace=True)
# original variable df -> value same
df
     

# describe()
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df.describe()



# Operation on Columns

import pandas as pd
d = {
    "name":["vishal","virat","vineet"], # 3 rows
    "salary":[100,200,300] # 3 rows
}
df = pd.DataFrame(data=d)
# add column
df["holidays"] = df["salary"] / 100
df["decrement"] = [10,20,30]
# delete column
df.drop(["salary","name"],axis=1,inplace=True)
df
     

import pandas as pd
d = {
    "name":["vishal","virat","vineet"], # 3 rows
    "salary":[100,200,300] # 3 rows
}
df = pd.DataFrame(data=d)
# add column
# df["marks"] = [10,20,30]
df["marks"] = df["salary"] / 2
df["increment"] = df["salary"] + (df["salary"] / 10)
# column name change
df.rename(columns={"increment":"salary_increment"},inplace=True)
df


import pandas as pd
df = pd.read_json("https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json")
df["marks"] = [10,20,30,40,50]
df["salary"]= [ 100,200,300,400,500]
df["marks"] = df["salary"] / 2
# print(df)
df["Increment"] = df["salary"]* 1.10
# print(df)

# column name change
df.rename(columns={"Increment":"salary_increment"},inplace=True)
print(df)
     


# Operation on Rows

import pandas as pd
d = {
    "name":["vishal","virat","vineet"], # 3 rows
    "salary":[100,200,300] # 3 rows
}
df = pd.DataFrame(data=d)
# print(df.loc[2,"name"])
# print(df.iloc[2,0])

# get single row data using iloc
# print(df.iloc[1])

# get single row using loc
# print(df.loc[1])

# get multi rows using iloc
# print(df.iloc[0:3])

# get multi rows using loc
# print(df.loc[0:3])

# sub data get using iloc
df1 = df.iloc[0:2,[0]] # rows -> 0,1 and cols -> 0 | name
df1

# sub data get using loc

     

# Filter DataFrame

import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
# filter 1
# df[df["english"] == 95]

# filter 2
df[df["maths"] < 60]

# physics values less than and equal to 56


# math 90 and english 90
df[(df["maths"] > 90)&(df["english"] > 90)]

# names
df[(df["maths"] > 90) & (df["english"]>90) & (df["gender"] == "Male")]["name"]
     

import pandas as pd
url = "https://raw.githubusercontent.com/SujaanBhalla/grrass-dsml/main/Python/data%201.csv"
df = pd.read_csv(url)
# print(df)
print(df[df["roll_no"]==2])



# Sorting

import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
# by default ascending
df.sort_values("english")

# decending
df.sort_values("english",ascending=False)

# by default ascending method 1
df.sort_values(by=['english'],ascending=[False])

# multiple cols sort
df.sort_values(by=['english'],ascending=[False])

# a to z
df['name'] = df['name'].str.lower()
df.sort_values("name")



# Operations on rows and columns
# add , update , delete

df
# add column total = py+math+english
df['total']  = df['english'] + df['maths'] + df['english']
df
# add row
df.loc[14] = ["rajendra",'Male',50,80,80,210]
df

# update column and update row

# delete column
df.drop("total",axis=1)

# delete row
df.drop(14,axis=0)

# delete row and delete column
df.drop()
     


# Working with Date Value

import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df['doj'] = ['2025-01-10','2025-02-10','2025-03-10','2025-04-10','2025-05-10']
df['doj'].dtype

# convert string to date
df['doj'] = pd.to_datetime(df['doj'])
df['doj'].dtype
# date operation
df['doj'].dt.year
df['doj'].dt.month
df['doj'].dt.day
df['doj'].dt.day_name()

# 20 days
df['doj'] + pd.to_timedelta(20,unit='D')
df['doj'] + pd.to_timedelta('20 days')



# Handling missing values

import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df.isnull()
# sum
df.isnull().sum()

# drop null values by row
df.dropna()

# drop null values by cols
df.dropna(axis=1)

# fill by zero
df.fillna(0)

# fill by 100
df.fillna(100)
df

# roll no -> 200 | marks -> 100 -> fillna
# method 1
# df["roll no"] = df['roll no'].fillna(200)
# df['marks'] = df['marks'].fillna(100)
# df

#method 2
# df.fillna({"roll no":200,"marks":100},inplace=True)
# df

# marks -> mean | nan fill with average
mm = df['marks'].mean()
df["marks"] = df['marks'].fillna(mm)
df


# Aggregation and group by

# aggregation
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
# manually
df['marks'].sum()
df['marks'].mean()
df['marks'].min()
df['marks'].max()
# usin aggregation
df['marks'].agg(["sum","mean","min","max"])



# Concatenate and merge dataframe (joins)

# concatenate
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df1 = pd.read_json(url)
# pd.concat([df,df1]) # row
pd.concat([df,df1],axis=1)

# name -> cols 2 -> abhishek -> rajendra
     
     
