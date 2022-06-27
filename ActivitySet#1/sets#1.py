 '''SET1 and SET2 are two sets that contain unique integers. SET3 is to be created by taking the union or intersection of SET1 and SET2 using the user defined function Operation(). Perform either union or intersection by reading choice from user. Do not use built in functions union() and intersection() and also the operators "|"and "&".'''
'''Expected Output

Enter Set1? 1 3 4 8
Enter Set2? 2 5 7 6
Enter operation (u/n)? u

Set3: 1 2 3 4 5 6 7 8'''
#CODE
def operation(s1,s2,op):
  if u == op:
    s3 = s1
    for ele in s2:
      if ele not in s3:
        s3.append(ele)
  elif n == op:
    s3 = []
    for ele in s1:
      if ele in s2:
        s3.append(ele)
  s3.sort()
  return s3

def main():
  Set1 = (input("Enter set1 elements ")).split(" ")
  Set2 = (input("Enter set1 elements ")).split(" ")
  Set3 = Operation(Set1,Set2,op)
  op = operation(Set1,Set2,op)
   print('Set3: ',end='')
  for ele in Set3:
    print(ele,'',end='')
main()
  

        
  