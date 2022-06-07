a = int(input())
for i in range(a):
  x1,y1,x2,y2,x3,y3= map(float, input().split())
  area=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y2-y1))
  print("Area of rectangle with vertices",(x1,y1),(x2,y2),(x3,y3),"is",area)
#Area of rectangle with vertices (0.0,0.0),(0.0,1.0),(1.0,0.0) is 1.0
#ActivitySet#3/problem#1.py