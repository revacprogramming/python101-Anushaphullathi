

class Menu(dict):
    """fill in class definition here"""
  def __init__(self):
    self.food = dict()
    
class Order:
    """fill in class definition here"""
   def __getvalue__(self,key):
      return(self.food[key])


class Bill:
    """fill in class definition here"""


m = Menu()
m["idly"] = 20
m["vada"] = 20

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)

b = Bill(m, o)
print(b)
