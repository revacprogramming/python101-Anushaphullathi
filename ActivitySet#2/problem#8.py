

class Menu:
    """fill in class definition here"""
      def __init__(self):
        self.list = dict()


    def add(self,x,n):
        if(x in self.list):
            self.list[x]+=n
        else:
            self.list[x]=n
    def show(self):
         for i in self.list:
             print(i,self.list)

    def __str__(self):
         s = ""
         for i in self.list:
             s+=i+" "+str(self.list[i])+"\n"
         return(s[:-1])

m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)
