#overiding
class Address:
    def __init__(self,city,state):
        self.city=city
        self.state=state
    def location(self):
        print("addresss location")

class User(Address):
    def __init__(self,name,age,city,state):
     super(). __init__(city,state)
     self.name=name
     self.age=age
    def location(self):   #overriding
       print("user locations")

u=User("arya mains",20,"kukas","rajasthan")
u.location()