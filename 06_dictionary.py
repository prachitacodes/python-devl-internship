#Q1
friend=["Prachita","Raj","Hira","Meera","Payo"]
t=[(i,len(i))for i in friend]
print("List of friends name=",friend)
print("list of tuples=",t)
#Q2

d1={"Hotel":1200,"Food":800,"Transportation":500,"Attractions":300,"Miscellaneous":200}
d2={"Hotel":1000,"Food":900,"Transportation":600,"Attractions":400,"Miscellaneous":150}
tot1=sum(d1.values())
tot2=sum(d2.values())
print("My total expenses=",tot1)
print("Partner's total expenses=",tot2)
if tot1>tot2:
    print("I spent more")
elif tot2>tot1:
    print("My partner spent more")
else:
    print("Both spent equally")
max_dif=0
max_cat=""   
for key in d1:
    dif=abs(d1[key]-d2[key])
    if dif>max_dif:
        max_dif=dif
        max_cat=key
print("Biggest Spending difference",max_cat,"by",max_dif)       
