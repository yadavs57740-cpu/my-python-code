#POLYMORPHISM

class Address:
  def __init__(self,city,state):
    self.city=city
    self.state=state
  def location(self):print(f"my address location is {self.city} in {self.state}")

class homeTown:
  def __init__(self,city,state):
    self.city=city
    self.state=state

  def location(self):
    print(f"my home town location is {self.city} in {self.state}")

a=Address("Vadodara","Gujarat")
a.location()
b=homeTown("Narnaul","Haryana")
b.location()