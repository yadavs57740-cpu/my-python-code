#CLASS VARIABLE

class Address:
  total=0  #class variable
  def __init__(self,city,state):
    self.city=city
    self.state=state
    Address.total+=1

  def location(self):
    print("location")

a=Address("jaipur","rajasthan")
b=Address("jalore","rajasthan")
a.total
