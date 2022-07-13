class Menu:
    """fill in class definition here"""
  def __init__(self):
   self.list = dict()

  def add(self,x,n):
    if(x in self.list()):
      self.list[x]+=n
    else:
      self.list():
      self.list[x]=n
  def show(self):
    for i in self.list():
      print(i,self.list())
      
m = Menu()  # Menu is a class#m is object
m+add("idly", 10)
m+("vada", 20)
print('idly ',m.idly)
print('vada ',m.vada)
m.show()
