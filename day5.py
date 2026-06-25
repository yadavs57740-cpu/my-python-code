#Importing & Using Modules

#import module
import math

print(math.factorial(5))
print(math.pow(5,2))
print(math.pi)
print(math.floor(10.7234))
print(math.ceil(10.0123))


# exmaple 1
import math as rajendra

# print(rajendra.factorial(5))
# print(rajendra.pow(5,2))
# print(rajendra.pi)
# print(rajendra.floor(10.7234))
# print(rajendra.ceil(10.0123))

# example 2
from math import factorial,pi

print(factorial(5))
print(pi)


# example 3
from math import *
print(pow(5,3))
print(pi)
print(floor(10.3211))


#File Handling

#Reading & Writing Files (txt, csv)

# from google.colab import drive
# drive.mount('/content/drive')

# file = open("/content/drive/MyDrive/hello.txt", "r")

# data = file.read()
# print(data)

# file.close()
     

# from google.colab import drive
# drive.mount('/content/drive')

# import csv

# with open("/content/drive/MyDrive/hello.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)
     


# Object Oriented Programming (OOP)

# Constructor (init)

# example
# class rajendra:
#   def __init__(self,name):
#     self.name = name
#   def show(self):
#     print(self.name)

# r = rajendra("hello")
# r.show()


#example 1
# class rajendra:
#   def __init__(self):
#     print("calling constructor")

#   def show(self):
#     print("show the name")

# r = rajendra()
# r.show()

# example 2
# self = {"fullname":"hello"}
# self.fullname = "hello"

# class rajendra:

#   def __init__(self,name,age):
#     self.fullname = name
#     self.age = age

#   def getAge(self):
#     print("My age is:",self.age)

#   def getName(self):
#     print("My name is:",self.fullname)

# r = rajendra("hello",20)
# r.getAge()
# r.getName()

# r = rajendra(age=20,name="hello")
# r.getAge()
# r.getName()



# example 3
# self = {"name":{"name":"hello","age":20}}
# self["name"]["name"]
# class student:
#   def __init__(self,args):
#     print(type(args))
#     print(args)
#     self.name = args

#   def getStu(self):
#     # print("the student is:",self.name)
#     return self.name


# s = student({"name":"hello","age":20}) # arguments -> 1,2
# t = s.getStu()
# print(t["age"])



#example 4
# class student:
#   def __init__(self,*args):
#     self.data = args

#   def users(self):
#     for i in self.data[0]:
#       print(i)

#   def details(self):
#     print(self.data[1])
#     for i in self.data[1]:
#       print()

# s = student(["dheeraj","kunal","harsh","praveen"],{"address":"kukas","college":"arya","loc":"jaipur"})
# s.details()



# class student:
#   def __init__(self,**args):
#     print(type(args))
#     print(args["name"])
#     self.data = args

#   def data(self):
#     print(self.data["name"])

# d = {}
# s = student(name="hello",age=20,users=["a","b","c"])
# # s.data()



# def stu(*a):
#   print(a)

# stu([10,20,40])


def stu(**a):
  print(a)

stu(name="hello",age=20)
     