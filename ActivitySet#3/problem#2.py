#python ActivitySet#3/problem#2.py
a = int(input())
for i in range(a):
    b=int(input())
    x=list(map(int,input().split()))
    sum=0
    for k in range(b-1):
      sum=sum+(1/x[0+k])
      #for l in range(b):
    print(f"{x} = {sum}")
