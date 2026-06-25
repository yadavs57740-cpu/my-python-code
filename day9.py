# Matplotlib

import matplotlib.pyplot as plt
score = [10,20,30,40]
over = [1,2,3,4]
plt.plot(score,over)

plt.show()


# 1 Create First Chart

import matplotlib.pyplot as plt # visualization
x = [2010,2015,2020,2025] # x cord
y = [100,200,250,300] # y cord.
plt.plot(x,y) # Line graph
plt.xlabel("years") # x label
plt.ylabel("sales") # y label
plt.title("sales report") # graph title
plt.show() # graph show



# 2 Customize Chart

import matplotlib.pyplot as plt
x = [2010,2015,2020,2025] # x cord
y = [100,200,250,300] # y cord.

#
# **Markers**

# |character      |  |  |description |
# |-------------|  -------------------------------|
# |'.'       | | |point marker|
# |','       | | |pixel marker|
# |'o'       | | |circle marker|
# |'v'       | | |triangle_down marker|
# |'^'       | | |triangle_up marker|
# |'<'       | | |triangle_left marker|
# |'>'       | | |triangle_right marker|
# |'1'       | | |tri_down marker|
# |'2'       | | |tri_up marker|
# |'3'       | | |tri_left marker|
# |'4'       | | |tri_right marker|
# |'8'       | | |octagon marker|
# |'s'       | | |square marker|
# |'p'       | | |pentagon marker|
# |'P'       | | |plus (filled) marker|
# |'*'       | | |star marker|
# |'h'       | | |hexagon1 marker|
# |'H'       | | |hexagon2 marker|
# |'+'       | | |plus marker|
# |'x'       | | |x marker|
# |'X'       | | |x (filled) marker|
# |'D'       | | |diamond marker|
# |'d'       | | |thin_diamond marker|
# |'|'       | | |vline marker|
# |'_'       | | |hline marker|

# **Line Styles**

# |character      |  |  |  |description |
# |-------------|   -------------------------------|
# |'-'       | | | |solid line style|
# |'--'      | | | |dashed line style|
# |'-.'      | | | |dash-dot line style|
# |':'       | | | |dotted line style|

# Example format strings:

#     'b'    # blue markers with default shape
#     'or'   # red circles
#     '-g'   # green solid line
#     '--'   # dashed line with default color
#     '^k:'  # black triangle_up markers connected by a dotted line
# **Colors**

# |character      |  |  |  |color |
# |-------------|   -------------------------------|
# |'b'       | | | |blue|
# |'g'       | | | |green|
# |'r'       | | | |red|
# |'c'       | | | |cyan|
# |'m'       | | | |magenta|
# |'y'       | | | |yellow|
# |'k'       | | | |black|
# |'w'       | | | |white|
# graph size
plt.figure(figsize=(6,2)) # width or height
plt.plot(x,y,color="y",marker='*',linestyle=":",linewidth=4,markersize=19,)
plt.show()
      


# 3 Advanced - Multiple Lines & Legends

# multi lines chart
import matplotlib.pyplot as plt

x = [2010,2015,2020,2025]
farming1 = [100,300,260,290]
farming2 = [150,185,400,300]

plt.plot(x,farming1,label="farming 1")
plt.plot(x,farming2,label="farming 2")
plt.legend() # info of label
plt.show()

# question on multiple line chart ->



# 4 Bar Chart

# bar chart
import matplotlib.pyplot as plt
x = [2015,2020,2025,2030]
y = [100,150,200,290]

# size
plt.figure(figsize=(6,2)) #
plt.bar(x,y)
plt.show()


# multi bar chart
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4])
y1 = [10,20,20,40]
y2 = [20,30,25,30]
# calculation -> width
w = 0.40
plt.bar(x - w/2,y1 , label="boys",width=w) # hide second
plt.bar(x + w/2,y2, label="girls",width=w) # show

plt.xlabel("groups")
plt.ylabel("number of students")
plt.title("Number of Students in Each group")
plt.legend()
plt.show()


# example
import matplotlib.pyplot as plt
import numpy as np

x= np.array([1, 2, 3, 4]) # x cord
y1 = [10, 20, 20, 40]
y2 = [20, 30, 25, 30] # y cord
y3 = [30, 40, 35, 20]

w = 1.00
plt.bar(x-0.33, y1, width=w/3, label="Boys")# bottom = y1
plt.bar(x, y2, width=w/3, label="Girls")
plt.bar(x+0.33, y3, width=w/3, label="Others")

plt.xlabel("Groups")
plt.ylabel("No of students")
plt.title("Students in each group")
plt.legend()
plt.show()
     


# 5 Histogram

import matplotlib.pyplot as plt
marks = [40,55,60,70,75,90,33,50]
plt.hist(marks,bins=5,color='green')
plt.show()



# 6 Pie chart

# pie chart
import matplotlib.pyplot as plt
fruits = ['apple','banana','orange','watermelon']
count = [40,30,15,70]
colors = ["red","yellow","orange","green"]
plt.pie(count, labels=fruits, colors=colors)
plt.show()


# pie chart percentage
import matplotlib.pyplot as plt
fruits = ['apple','banana','orange','watermelon']
count = [40,30,15,70]
colors = ["red","yellow","orange","green"]
plt.pie(count,labels=fruits,colors=colors,startangle=90,autopct="%1.1f%%")
plt.show()
     


# 7 Subplot | Subplots

import matplotlib.pyplot as plt

# subplot
# first chart
x = [1,2,3,4,5]
y = [10,20,30,40,55]

plt.subplot(2,2,1) # row,cols,position
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")

# second chart
x1 = ['apple','banana','orange','watermelon']
y1 = [40,30,15,70]

plt.subplot(2,2,2) # row,cols, position
plt.pie(y1,labels=x1,startangle=90)
plt.xlabel("x1 axis")
plt.ylabel("y1 axis")

# third chart
x = [1,2,3,4,5]
y = [10,20,30,40,55]

plt.subplot(2,2,3) # row,cols,position
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
# fourth chart
x1 = ['apple','banana','orange','watermelon']
y1 = [40,30,15,70]

plt.subplot(2,2,4) # row,cols, position
plt.pie(y1,labels=x1,startangle=90)
plt.xlabel("x1 axis")
plt.ylabel("y1 axis")


plt.tight_layout()
plt.show()



# subplots
import matplotlib.pyplot as plt
# graph one data
year = [2010,2015,2020,2025]
dairy = [100,520,630,400]

# graph two data
year = [1990,2000,2005,2010]
farming = [300,200,250,100]

fig , aux = plt.subplots(1,2)
# this is first graph
aux[0].plot(year,dairy) # first col for line chart
aux[0].set_xlabel("year")
aux[0].set_ylabel("dairy")
aux[0].set_title("dairy production graph")

# this is second graph
aux[1].plot(year,dairy) # first col for line chart
aux[1].set_xlabel("year")
aux[1].set_ylabel("farming")
aux[1].set_title("farming production graph")

plt.show()



# subplots 2d
import matplotlib.pyplot as plt

year = [2010,2015,2020,2025]
dairy = [100,520,630,400]

farming = [300,200,250,100]

college = [10,20,25,30]

transport = [50,75,100,150]

fig,aux = plt.subplots(2,2) # 4 cols
# first row and first cols
aux[0][0].plot(year,dairy)
aux[0][0].set_xlabel("year")
aux[0][0].set_ylabel("dairy")
aux[0][0].set_title("dairy production")

aux[0][1].bar(year,farming)
aux[0][1].set_xlabel("year")
aux[0][1].set_ylabel("farming")
aux[0][1].set_title("farming production")

aux[1][0].pie(college,labels=year)
aux[1][0].set_xlabel("year")
aux[1][0].set_ylabel("college")
aux[1][0].set_title("college production")

aux[1][1].scatter(year,transport)
aux[1][1].set_xlabel("year")
aux[1][1].set_ylabel("transport")
aux[1][1].set_title("transport production")


plt.tight_layout()

plt.show()


# example
students = ["A", "B", "C", "D", "E"]
marks = [85, 90, 75, 88, 95]

attendance = [80, 90, 75, 85, 95]

ages = [18, 19, 18, 20, 19]

fig, ax = plt.subplots(2, 2)

# Line Chart
ax[0,0].plot(students,marks,marker='o')
ax[0,0].set_title("Marks Trend")
ax[0,0].set_xlabel("Students")
ax[0,0].set_ylabel("Marks")
ax[0,0].grid(True)

# Bar Chart
ax[0,1].bar(students,attendance,color="orange")
ax[0,1].set_title("Attendance")
ax[0,1].set_xlabel("Students")
ax[0,1].set_ylabel("Attendance %")

# pie char
ax[1,0].pie(ages,labels= students)

# Histogram
ax[1,1].hist(marks,bins=5,color="green",edgecolor="black")
ax[1,1].set_title("Marks Distribution")
ax[1,1].set_xlabel("Marks")
ax[1,1].set_ylabel("Frequency")

plt.tight_layout()


# plt.gcf().canvas.get_supported_filetypes()
plt.savefig("subplot1.pdf")
plt.show()



# 8 Scatter plot
# 9 Matplotlib with Pandas - real data
# 10 Save charts

import pandas as pd
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-arya/main/temperature_data.json"
df = pd.read_json(url)

# drop row 3 -> day = wednesday
df.dropna(subset=["temperature_c"],inplace=True)
df

# fill average value -> humidity -> nan
df.fillna(df['humidity_pct'].mean(),inplace=True)
df

# new cols -> farenheit   | cell*1.8 -> + 32
df['temperature_f'] = (df['temperature_c'] * 1.8)+32
df
# subplots -> 1d -> line chart | pie chart
fig,aux = plt.subplots(1,2)
aux[0].plot(df["humidity_pct"],df["temperature_c"])
aux[0].set_xlabel("humidity")
aux[0].set_ylabel("temperature in celsius")
aux[0].set_title("humidity with celsius")

aux[1].pie(df["temperature_f"],labels=df["day"],autopct="%1.1f%%")
aux[1].set_title("humidity with farenheit")
# save image data
plt.savefig("project1.pdf")
plt.show()
     


df = pd.read_json("https://raw.githubusercontent.com/rajendra0968jangid/Ds-arya/main/temperature_data.json")
df.drop(2, inplace=True)
df["humidity_pct"]=df["humidity_pct"].fillna( df["humidity_pct"].mean() )
df["In_Farehneit"] = (df["temperature_c"] * 1.8) + 32

fig,aux=plt.subplots(2,2)

# first graph -> pie chart
aux[0,0].pie(df["temperature_c"],labels= df["day"], autopct="%1.1f%%",shadow= True, explode=[0.1,0,0,0,0,0],wedgeprops={"edgecolor":"black","width" : 0.4})
aux[0,0].set_title("Celsius Graph")

# second graph -> pie chart
aux[0,1].pie(df["humidity_pct"],labels= df["day"], autopct="%1.1f%%",shadow= True,explode=[0.1,0,0,0,0,0],wedgeprops={"edgecolor":"black","width" : 0.4})
aux[0,1].set_title("Humidity Graph")

# third graph -> pie chart
aux[1,0].pie(df["In_Farehneit"],labels= df["day"], autopct="%1.1f%%", shadow= True, explode=[0.1,0,0,0,0,0],wedgeprops={"edgecolor":"black","width" : 0.4})
aux[1,0].set_title("Farihneit Graph")

# fourth graph -> line graph
aux[1,1].plot(df["temperature_c"],df["In_Farehneit"],marker='o')
aux[1,1].set_title("Celsius vs Fahrenheit")
aux[1,1].set_xlabel("Celsius")
aux[1,1].set_ylabel("Fahrenheit")
aux[1,1].grid(True)

plt.gcf().canvas.get_supported_filetypes()
plt.savefig("subplots.jpg")

plt.tight_layout()

plt.show()