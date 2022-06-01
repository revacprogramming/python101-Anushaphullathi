# Conditional Execution
score = input("Enter Score between 0.0 and 1.0 : ")
sr=float(score)
 
if sr >= 0.9 :
    print("A")
elif sr>=0.8 :
    print("B")
elif sr>=0.7 :
    print("C")
elif sr>=0.6 :
    print("D")
elif sr<0.6 :
    print("F")
else :
    quit()