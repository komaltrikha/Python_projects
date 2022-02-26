#!/usr/bin/env python
# coding: utf-8

# # Yummy In Your Tummy :)
# 

# In[2]:


menu = input('what would you like to eat ? \n1: pizza \n2: burger \n3: hotdog \n4: combo meal\n ')
bill = 0
meal1='pizza,fries,coke'
meal2='burger,fries,coke'
meal3='hotdog,fries,coke'
if menu=='pizza' or menu=='burger' or menu=='hotdog' or menu=='combo meal':
    if menu=='pizza':
        top = input("let's put something on the top ? \n1: cheese \n2: mushroom \n3: corn\n")
        if top  == 'cheese':
            bill = bill+240
            print('your bill amount is :', bill)
        elif top  == 'mushroom':
            bill = bill+260
            print('your bill amount is :', bill)
        elif top  == 'corn':
            bill = bill+280
            print('your bill amount is :', bill)
        else :
            print('your bill amount is : 200')
        
        
    elif menu=='burger':
        fill = input("let's fill it with : \n1: onion \n2: aloo tikki \n3: chicken\n")
        if fill=='onion':
            bill = bill+120
            print('your bill amount is :', bill)
        elif fill=='aloo tikki':
            bill = bill+140
            print('your bill amount is :', bill)
        elif fill=='chicken':
            bill = bill+160
            print('your bill amount is :', bill)
        else :
            print('your bill amount is : 100')
        
    
    elif menu=='hotdog':
        fil = input("let's fill it with : \n1: chilli \n2: salad \n3: pickles\n")
        if fil=='chilli':
            bill = bill+60
            print('your bill amount is :', bill)
        elif fil=='salad':
            bill = bill+70
            print('your bill amount is :', bill)
        elif fil=='pickles':
            bill = bill+80
            print('your bill amount is :', bill)
        else:
            print('your bill amount is 50')
    
    
    elif menu=='combo meal':
        print('meal1=pizza,fries,coke')
        print('meal2=burger,fries,coke')
        print('meal3=hotDog,fries,coke')
        
        meal=input('choose our meal options :\n1: meal1, \n2: meal2,\n3: meal3\n')
        if meal=='meal1':
            print('your bill amount is :300')
        elif meal=='meal2':
            print('your bill amount is :280')
        elif meal=='meal3':
            print('your bill amount is :260')
        else:
            print('Try something else')
            
            
    else:
        print ('not valid')
    
else:
    print('not available')


# In[ ]:




