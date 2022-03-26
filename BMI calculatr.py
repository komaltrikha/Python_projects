#!/usr/bin/env python
# coding: utf-8

# # Body mass index(BMI) calculator
# 

# In[5]:


Hf= float(input('enter you height in feet'))
Hi= float(input('enter you height in inches'))
h = (Hf*30.48)+(Hi*2.54)
w= float(input('enter your weight in kilogram :'))
##bmi=(w(kg)/h**2(meter))
bmi= (w/h**2)*10000
print(bmi)

if bmi>25:
    print('Over Weight : You need to subtract carbs')
elif bmi<=24.9 and bmi>18.5:
    print('Normal : You need to take 100gm of protien per day')
elif bmi<=18.5:
    print('Under Weight : You need to add carbs in your diet')
else:
    print('Invalid Credentials')
    
#1 foot = 30.48 centimeters.
#1 inch = 2.54 centimeters.
#To convert kg into pounds you have to multiply it by 2.205
#A BMI below 18.5 means that you are underweight.
#A BMI of 18.6 to 24.9 is healthy.
#A BMI of 25 to 29.9 means that you are overweight.
#A BMI of 30 or greater indicates obesity.


# In[ ]:




