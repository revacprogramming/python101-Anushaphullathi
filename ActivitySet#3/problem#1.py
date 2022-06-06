import math
a = int(input())
for i in range(a):
  l = list(map(float, input().split()))
  t = math.sqrt((l[0][0] - l[0][1])**2+(l[1][0] - l[1][1]**2))
  h = math.sqrt((l[2][0] - l[3][0])**2 + (l[2][1] - l[3][1])**2)
  area = t*h
  print("Area of rectangle with vertices",l[0],l[1],l[2],l[3],"is",area)
#Area of rectangle with vertices (0.0,0.0),(0.0,1.0),(1.0,0.0) is 1.0
