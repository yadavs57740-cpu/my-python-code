# Handle Missing values
import pandas as pd
data = {
    'Name':['Ram','Kamal','Ajay'],
    'Age':[25,None,32],
    'Salary':[5000,6000,None]
}
df=pd.DataFrame(data)
print("Original DataFrame")
print(df)

# null findout | fillna | dropna
df_drop = df.dropna()
print(df.drop)

#fill
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df)

print(df.isnull().sum())  #sum of null


# encoding
from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {
    'Name':['Ram','Kamal','Ajay','Neetu','Kavi','Sapu'],
    'Age':[25,None,32,20,21,22],
    'Salary':[5000,6000,None,7000,8000,9000],
    'Gender':['male','male','male',None,'female','female']
}

df = pd.DataFrame(data)
print("Original dataframe")
print(df)

# label encoder
le = LabelEncoder()
df_label = df.copy()
df_label['Gender'] = df['Gender'].fillna('unknown')
df_label['Gender_encoder'] = le.fit_transform(df_label['Gender'])
print("After label encoding:")
print(df_label)

# one hot encoding
import pandas as pd
data = {
    'colors':['red','blue','green','red','blue']
}

df = pd.DataFrame(data)
print("original data")
print(df)

encoded_df = pd.get_dummies(df,columns=['colors'])

print("after one hot encoding")
print(encoded_df)