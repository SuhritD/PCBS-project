# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:11:25 2019

@author: Suhrit
"""

def F2C(temp):
    print("Your converted temperature is ",str((temp-32)*5/9)," C")
    
def C2F(temp):
    print("Your converted temperature is ", str(temp*1.8+32)," F")

temp = input("Enter the temperature.")
x = input("Enter the unit of temperature, C/F ")
if (x=='C' or x=='c'):
    C2F(float(temp))
elif(x=='F' or x=='f'):
    F2C((temp))
else:
     "Invalid input."
     
