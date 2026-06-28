# feature scaling
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
 
data = {
    "experience":[300,600,900,1500],
    "salary":[1000,1500,2000,3000]
}
# data frame
df = pd.DataFrame(data)
print(df)
 
# standard scaler
scaler = StandardScaler()
df['experience'] = scaler.fit_transform(df[['experience']]) # 2d
print(df)
 
# split data exp-> x | sal -> y
X = df['experience'] # capital X
y = df['salary']
 
print(X)
print(y)
 
# graph plot
plt.plot(X , y)
plt.title("Experience vs Salary ")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()



# data split training testing
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
 
data = {
    "experience":[300,600,900,1500],
    "salary":[1000,1500,2000,3000]
}
 
df = pd.DataFrame(data)
print(df)
 
# split data
X = df['experience'] # capital X
y = df['salary']
 
# train test split
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
print("x train: ",x_train)
print("x test: ",x_test)
print("y train: ", y_train)
print("y test: ", y_test)
 
 
 # data split training testing
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
 
data = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/extended_salary_data.csv"
 
df = pd.read_csv(data)
# print(df)
 
# split data
X = df['experience'] # capital X
y = df['salary']
 
# train test split
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print("x train: ",x_train )
print("x test: ",x_test)
print("y train: ", y_train)
print("y test: ", y_test)
 

 
 # simple linear reg | prediction
from sklearn.linear_model import LinearRegression
 
# model fit
model = LinearRegression()
model.fit(x_train,y_train) # 2d
 
# input from user
user = int(input("Enter your Experience: "))
# model prediction
 
new_data = {
    "experience":[user]
}
 
df1 = pd.DataFrame(new_data)
print(df1)
pred_data = model.predict(df1)
print(pred_data[0])