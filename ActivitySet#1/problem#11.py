# Tuples

filename = "dataset/mbox-short.txt"

filename = "dataset/mbox-short.txt"
name=input("Enter the file name:","r")
fhand=open(name)
fread=fhand.readlines()
d=dict()
for line in fread:
    if line.startswith("From "):
        l=line.strip()
        l=l.split()
        l=l[5]
        l=l[0:2]
        d[l]=d.get(l,0)+1
        term=sorted([(v,c) for v,c in d.items()])
for v,c in term:
    print(v,c)
..




#name = input("Enter file:","r")
#fhandle = open(name)
#d=dict()
#for line in fhandle:
#    if not line.startswith("From "):
#        continue
#    l=line.split()
#    l=l[5]
#    l=l[0:2]
#    d[l]=d.get(l,0)+1
#tem=sorted([(v,c) for v,c in d.items()])

#for v,c in tem:
#    print(v,c)