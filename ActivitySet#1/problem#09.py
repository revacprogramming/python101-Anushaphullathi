# Lists
filename = "dataset/romeo.txt"
filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.strip()
    words=line.split()
    for nword in words:
        if not nword in lst:
            lst.append(nword)       
lst.sort()
print(lst)

# or
#method-2/

#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#    words=line.strip().split()
#    for nword in words:
 #       if not nword in lst:
  #          lst.append(nword)       
#lst.sort()
#print(lst)

#or
#method-3

#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
 #   words=line.strip().split()
 #   for nword in words:
#        if nword in lst:
 #           continue
  #      else:
   #         lst.append(nword)       
#lst.sort()
#print(lst)

#or
#method-4

#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#    words=line.strip().split()
#    for nword in words:
#        if nword in lst:
#            continue
#        elif nword not in lst:
#            lst.append(nword)
#lst.sort()
#print(lst)