#Q1
h=float(input("Enter height in metres"))
w=float(input("Enter weight in kilograms"))
bmi=w/(h**2)
print(bmi)
if bmi>=30:
    print("Obesity")
elif bmi>=25 and bmi<=29:
    print("Overweight")
elif bmi>=18.5 and bmi<=25:
    print("Normal")        
else:
    print("Underweight")
#Q2
Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]
city=input("Enter a city name:")
if city in Australia:
    print(city,"is in Australia")
elif city in UAE:
    print(city,"is in UAE")
elif city in India:
    print(city,"is in India")
else:
    print(city,"is not in Australia,UAE,India")
#Q3
Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]
c1=input("Enter first city")
c2=input("Enter second city")
if c1 and c2 in Australia:
    print("Both cities are in Australia")
elif c1 and c2 in UAE:
    print("Both cities are in UAE")
elif c1 and c2 in India:
        print("Both cities are in India")
else:
    print("They don't belong to the same city ")




