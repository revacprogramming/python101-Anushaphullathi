# Dictionaries

filename = "dataset/mbox-short.txt"
#method-1

filename = "dataset/mbox-short.txt"
count=dict()
name = input("Enter the file name:")
handle = open(name,'r')
for line in handle:
    if not line.startswith('From '): 
        continue
    words=line.split()
    words=words[1]
    count[words]=count.get(words,0)+1
print(words, count[words])

#method-2

#filename = "dataset/mbox-short.txt"
#count=dict()
#name = input("Enter the file name:")
#handle = open(name,'r')
#for line in handle:
 #   if line.startswith('From '): 
#    words=line.split()
#    words=words[1]
#    count[words]=count.get(words,0)+1
#print(words, count[words])

#method-3

#filename = "dataset/mbox-short.txt"
#count=dict()
#name = input("Enter the file name:")
#handle = open(name,'r')
#for line in handle:
#    if line.startswith('From '): 
#        words=line.split()
#        words=words[1]
#        count[words]=count.get(words,0)+1
#    else :
#      continue
#print(words, count[words])

#method-4

#filename = "dataset/mbox-short.txt"
#count=dict()
#name = input("Enter the file name:")
#handle = open(name,'r')
#for line in handle:
#    if not line.startswith('From '): 
#        continue
#    elif line.startwith('From '):
#        words=line.split()
#        words=words[1]
#        count[words]=count.get(words,0)+1
#print(words, count[words])