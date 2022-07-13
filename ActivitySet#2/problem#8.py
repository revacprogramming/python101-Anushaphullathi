

class Menu:
    """fill in class definition here"""
    def __init__(self):
        self.food = dict()
    def __getvalue__(self,key):
      return(self.food[key])
         
    def __setvalue__(self,values):
        if(value in self.food):
            self.list[key]+=value
        else:
            self.list[key]=value
         
    def __str__(self):
         s = ""
         for i in self.list:
             s+=i+" "+str(self.food[i])+"\n"
         return(s[:-1])

m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)
