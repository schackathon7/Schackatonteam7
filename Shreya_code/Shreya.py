#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Capital=int(input())
Target_amount=int(input())
S=(input("Enter Monthly or Yearly"))


if(Capital<0):
    print ("error")
elif(Target_amount<0):
    print ("error")
elif(Target_amount<=Capital):
    print ("error")
elif(n<0):
    print ("error")


if (Capital>=100000):
    r=3
    
elif(100000>Capital>50000):
        r=2.5
elif(Capital<50000):
        r=2
R=r/100
if(S=="Yearly"):
    n=int(input("Enter no of years:"))
    p= 1+ (R)
    Yearly_our_payment=Target_amount-(Capital*(p ** n))
    Yearly_our_payment=Yearly_our_payment/n
    print(Yearly_our_payment)

elif(S=="Monthly"):
    n=int(input("Enter no of months:"))
    p= 1+(R/12)
    Monthly_our_payment=Target_amount-(Capital*(p ** n))
    Monthly_our_payment=Monthly_our_payment/n
    print(Monthly_our_payment)


# In[ ]:




