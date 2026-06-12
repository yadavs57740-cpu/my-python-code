# inheritance

#example 1
class Address:
  def __init__(self,city,state):
   self.city=city
   self.state=state

  def location(self):
    return f"my location is {self.city} in {self.state}"
  
class User(Address):
    def __init__(self,name,age,city,state):
     super(). __init__(city,state)
     self.name=name
     self.age=age
    #   self.city=city   #super()
    #   self.state=state

    def userName(self):
      print(f"my name is {self.name}")

    def userDetails(self):
      print(f"my name is {self.name} and my location is {self.city} in {self.state}")

u= User("nikita",20,"kukas","rajasthan")
print(u.city)
u.userDetails()
u.location()
 
#a = Address("kukas","rajasthan")