#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ECOMMERCE DISCOUNTS AND OFFERS
def big_sales ():
    product=input('please select your product : \n1: electronics \n2: appearls \n3: baby products \n4: personal care\n')
    product = product.lower()
    if product=='electronics' or  product=='appearls' or  product=="baby products"  or product=='personal care':
        if product=='electronics':
            on=input('select from these : \n1: phones \n2: laptops \n3: ac & fridge\n')
            on = on.lower()
            if on=='phones':
                print('we have 10% off on price')
            elif on=='laptops':
                print('we have 5% off on price')
            elif on=='ac' or "&" or "fridge":
                print('we have 20% off on price')
            else:
                print('invalid')
        elif product=='appearls':
            
            you=input('select from these : \n1: male \n2: female\n')
            you = you.lower()
            if you=='male':
                print('sorry we have no discount for u')
            elif you=='female':
                print('we have 5% off on price')
            else:
                print('not avl')
        elif product=='baby products' :
            print('we have 40% off on price')
            
        elif product=='personal care':
            print('shop above 600 to get 50% off')
        else:
            ('not available anything for u')
    else:
        print('sorry we dont have this')
        
big_sales()


# In[ ]:




