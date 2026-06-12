#oops

#CONSTRUCTOR
#example 1
class nikita:
  def __init__(self,name):  #constructor
    self.name=name
  def show(self):
    print(self.name)

n = nikita("hello")  #object
n.show()

#example 2
class nikita:
  def __init__(self):
    print("calling constructor")

  def show(self):
    print("show the name")

n=nikita()
n.show()

#example 3
class nikita:
  def __init__(self,name,age): 
    self.name=name
    self.age=age

  def getAge(self):
    print("My age is:",self.age)

  def getName(self):
    print("My name is:",self.name)   

n=nikita("hello",20)
n.getAge()
n.getName()

#example 4
class student:
  def __init__(self,*args):
    print(type(args))
    print(args)
    self.name=args[0]

  def getStu(self):
   # print("the student is:",self.name)
    return self.name

s=student("hello",20,"0000000000","arya@gmail.com")
# s.getStu()
t=s.getStu()
print(t)


#example 5
class student:
  def __init__(self,*args):
    print(type(args))
    print(args)
    self.name=args

  def getStu(self):
   # print("the student is:",self.name)
    return self.name

s=student({"name":"hello","age":20})  # 1 argument
t=s.getStu()
print(t)   #t["age"]

#example 6
class student:
  def __init__(self,*args):
    self.data=args

  def users(self):
    for i in self.data[0]:
      print(i)
  
  def details(self):
    for i in self.data[1]:
      print(i,":",self.data[1][i])
 
  
s=student(["dheeraj","kunal","harsh","praveen"],{"address":"kukas","college":"arya","location":"jaipur"})
s.users()
s.details()

#example 7
class student:
  def __init__(self,**args):
    print(type(args))
    print(args["name"])
    self.data=args

  def data(self):
    print(self.data["name"])

d={}
s=student(name="hello",age=20,users=["a","b","c"])
#s.data()



class student:
  def __init__(self,name,age):
    print(type(name))
    print(args)
    self.data=args

  def data(self):
    print(self.data["name"])

s=student(name="hello",age=20,users=["a","b","c"])
s.data()

#example9
class Address:
 city="jaipur"
 state="rajasthan"
 def __init__(self,city,state):
   self.city=city
   self.state=state

a=Address("jaipur","rajasthan")
print(a.city)


class Address:
 def __init__(self,city,state):
   self.city=city
   self.state=state

 def show(self):
   print("the city is:","rajasthan")

a=Address()
