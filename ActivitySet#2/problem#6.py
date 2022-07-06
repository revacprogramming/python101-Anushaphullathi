

class Menu:
    """fill in class definition here"""
  def __init__(self,idly,vada):
    self.idly = idly
    self.vada = vada
    
m = Menu()  # Menu is a class#m is object
m.add("idly", 10)
m.add("vada", 20)
print('idly ',m.idly)
print('vada ',m.vada)
m.show()
