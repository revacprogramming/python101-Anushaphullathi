# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
a=input("Enter the file name: ")
b=open(a)
c=re.findall("[0-9]+", b.read())
sum=sum([int(i) for i in c])
print(sum)
#short hand form
#import re
#print(sum([int(i) for i in re.findall("[0-9]+",open(name).read())]))
#python ActivitySet01/problem12.py
#ActivitySet01/final.txt
#451824..