#!/usr/bin/env python
# coding: utf-8

# In[10]:

#Amount you can to invest for now:
capital=float(input())

#Amount you want at the end of your plan:
final=float(input())



#Whether you want to save the money monthly or yearly
s=input("Enter Yearly or monthly:")

#Checking invalid output
if(capital<0):
    print("Invalid capital amount")
    
#Setting interest rates in the backend   

elif(capital<1000):
    r=2
elif (capital>=1000 and capital <=10000):
    r=2.5
elif (capital>10000 and capital <=30000):
    r=3
elif (capital>30000 and capital <=50000):
    r=3.5
elif (capital>50000 and capital <=80000):
    r=4
elif (capital>80000 and capital <=100000):
    r=4.5
else:
    r=5


# In[8]:

#Checking invalid output if Final amount is lesser than or equal to capital 
if (final <=0 or final<capital):
    print("Invalid Amount")
elif (final==capital):
    print(0)

#Checking invalid output if Final amount is lesser than or equal to capital 

#Calculating the amount she has to save each month or year

else:
    if(s=="Yearly" or s=="yearly"):
        n=int(input("Enter no of years:"))
        if(n<=0):
           print("Invalid no of years")
        else:
           base= 1+ (r/100)
           a1=capital*(base ** n)
           a=final-a1
           a=a/n
           print(a) #Amount she has to save Yearly

    else:
        n=int(input("Enter no of months:"))
        if(n<=0):
           print("Invalid no of months")
        else:
           base= 1+ (r/100)
           a1=capital*(base ** n)
           a=final-a1
           a=a/n
           print(a) #Amount she has to save Monthly
