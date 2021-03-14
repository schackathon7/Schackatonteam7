#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Amount you can to invest:
capital=float(input("Enter the amount you can to invest:"))

#Amount you want to invest yearly or monthly:
amount=float(input("Enter the amount you want to invest:"))
s=input("Enter yearly or monthly:")

#Expected rate of interest:
roi=float(input("You expect the Annual Rate of Returns to be:"))


#Declaring variables

b=[]
c=[]
result=capital


# In[3]:
#Checking for invalid values

if (capital<0):
    print("Invalid Capital Amount")
    
elif (amount <=0):
    print("Invalid Amount")
    
elif (roi <=0):
    print("Invalid rate of Interest")
    
elif (duration <=0):
    print("Invalid duration")
    
    
#To calculate the increase in the capital amount wrt rate of interest and Amount that we are investing monthly/yearly

else:
    if timeline == "years":
        for i in range(0,duration):
            result = amount+result
            c.append(result)
        for i in range(0,duration):
            result=capital_amount*(1+(roi/100))
            capital_amount=amount+result
            b.append(result+100)
        print(result+amount)
    else:
        for i in range(0,duration):
            result = amount+result
            c.append(result)
        for i in range(0,duration):
            result=capital_amount*(1+(roi/100*12))
            capital_amount=amount+result
            b.append(result+amount)
        print(result+amount)



#The predicted amount for the n of years 

print(result+amount)


#The increase in amount for each year for the timeline with interest rate
b


#The increase in amount for each year for the timeline without interest rate

c


#OUTPUT

print("After",n,"years/months, your investment of ",c[-1]," lakhs will grow to ₹",b[-1]," * @ ",r," % p.a")

