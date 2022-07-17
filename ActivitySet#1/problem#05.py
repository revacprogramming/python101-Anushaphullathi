# Functions
def computepay(h,r) :
    if h < 40 :
        p= h*r
    elif h > 40 :
        p= 40*r + (h-40)*1.5*r
    return p
  

hrs = float(input("Enter hours : "))
rt = float(input("Enter the rate : "))
p = computepay(hrs,rt)
print("Pay",p)