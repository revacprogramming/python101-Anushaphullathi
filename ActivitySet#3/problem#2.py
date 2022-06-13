#python ActivitySet#3/problem#2.py
'''''a = int(input())
for i in range(a):
    b=int(input())
    x=list(map(int,input().split()))
    sum=0
    for k in range(b-1):
      sum=sum+(1/x[0+k])
      #for l in range(b):
    print(f"{x} = {sum}")'''''
import math
def get_fraction(l):
    num=0
    den=1
    for i in l:
      den*=i
    for i in l:
      num+=den/i
    gcd=math.gcd(int(den),int(num))
    return([int(num/gcd),int(den/gcd)])

def get_num():
    a=int(input())
    for i in range(a):
      b=int(input())
      x=list(map(int,input().split()))
      k=get_fraction(x)
      for i in x[:-1]:
        print(f"1/{i} ",end="+ ")
      print(f"1/{x[b-1]} = {k[0]}/{k[1]}")
get_num()


    

  
