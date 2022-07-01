# Object Oriented Programming
# https://www.py4e.com/lessons/Objects
'''Lab Program 5a:
A "Car" has the attributes Company_name, model, color, Manufacuting_year and price.  A Class is required to be created for "Car" to store the above attributes and perform the following operations:
i) Get the details of “Car” object from user and store into Array of objects.
ii) Display the details of “Car” object based on “Company”, “Model” and “Price”.'''

#Code
class car:
    def __init__(self,year,company,model,speed,price):
        self.year=year
        self.company=company
        self.model=model
        self.speed=speed
        self.price=price
    def display_car_details(self):
        print(self.year,"\t",self.company,"\t",self.model,"\t",self.speed,"\t",self.price)
carobject=[]
n=int(input("How many car details you want to enter"))
for i in range(n):
    year=int(input("Enter Manufacturing year\n"))
    company=input("Enter Manufacturing Company\n")
    model=input("Enter Model\n")
    speed=float(input("Enter the speed\n"))
    price=float(input("Enter the price of Car\n"))
    carobject.append(car(year,company,model,speed,price))
print("Car Details are\n")
for obj in carobject:
    obj.display_car_details()
  
'''Lab Program 5b:       
Airline Reservation System contains the attributes of passengers such as Name, PAN-No., Mobile-no, Email-id, Source, Destination, Seat-No and Air-Fare, Travel_date. A Class is required to be created for "Airlilne" with the above attributes and perform the following operations:
a. Get the details of "Airline" object from user and store into Array of objects
b. List details of all the passengers who travelled From "Bengaluru to London".
c. List details of all the passengers who travelled From "USA to China" on 10th of Feb, 2020.'''

#Code

Airlineobject=[ ]
class ARS:
    def __init__(self,name,source,destination,travel_date):
        self.name=name
        self.source=source
        self.destination=destination
        self.travel_date=travel_date
    def display_pass_details(self):
         print(self.name,"\t",self.source,"\t",self.destination,"\t",self.travel_date)
Airlineobject.append(ARS("Sachin","bangalore","USA","1/oct/2020"))
Airlineobject.append(ARS("Dravid","bangalore","London","2/oct/2020"))
Airlineobject.append(ARS("Rahul","bangalore","China","3/oct/2020"))
Airlineobject.append(ARS("Kiran","bangalore","London","5/oct/2020"))
Airlineobject.append(ARS("Supreeth","USA","China","10/Feb/2020"))

print("Details of the Passenger who travelled from bangalore to London is \n")
for i in range(0,len(Airlineobject)):
    if((Airlineobject[i].source=="bangalore") and (Airlineobject[i].destination=="London")):
        Airlineobject[i].display_pass_details()
print("\n")
print("Details of the Passenger who travelled from USA to China on 10th Feb 2020 is \n")
for i in range(0,len(Airlineobject)):
    if((Airlineobject[i].source=="USA") and (Airlineobject[i].destination=="China") and Airlineobject[i].travel_date=="10/Feb/2020"):
        Airlineobject[i].display_pass_details()




