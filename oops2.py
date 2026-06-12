# ENCAPSULATION
class Address:
  def __init__(self,city,state):
    self.__city=city # private attribute
    self.state=state
  def location(self):
    print(f"my location is {self.__city} in {self.state}")

  def get_city(self):
    return self.__city

a=Address("Narnual","Haryana")
a.location()
a.get_city()
#print(a.city)
print(a.state)
