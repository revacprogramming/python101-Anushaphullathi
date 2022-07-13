
class Menu:
    """fill in class definition here"""
    def __init__(self):
        self.list = dict()


    def __add__(self,t):
        x=t[0]
        n=t[1]
        if(x in self.list):
            self.list[x]+=n
        else:
            self.list[x]=n
        return(self)
    def show(self):
         for i in self.list:
             print(i,self.list)

    def __str__(self):
         s = ""
         for i in self.list:
             s+=i+" "+str(self.list[i])+"\n"
         return(s[:-1])


m = Menu()
m+('idly',10)+("pongal",20)
print(m) # should print the menu properly
