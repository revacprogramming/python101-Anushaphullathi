# Files

filename = "dataset/mbox-short.txt"
name=input("Enter the file name: ","r")
fhand=open(name)
sm=0
count=0
fread=fhand.readlines()
for line in fread:
    if line.startswith("X-DSPAM-Confidence:"):
        sm+=float(line.split()[1])
        count+=1
print(f"Average spam confidence: {sm/count}")