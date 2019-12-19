# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:17:18 2019

@author: Suhrit
"""''
import numpy as np, matplotlib.pyplot as plt
p0={(1,2):0.1,(2,3):0.1,(3,5):0.1,(2,4):0.1,(3,6):0.1}
p1={(1,2):0.9,(2,3):0.9,(3,5):0.9,(2,4):0.9,(3,6):0.9}
ep0={(1,2):0.1,(2,3):0.1,(3,5):0.1,(2,4):0.1,(3,6):0.1}
ep1={(1,2):0.9,(2,3):0.9,(3,5):0.9,(2,4):0.9,(3,6):0.9}
a11=a10=a00=a01=[]
x=np.zeros(7)
LOR=[]
asc=desc=1
def wt(a,b,c): #weights of the messages
    if(b>a):
      w=(ep1[a,b]*np.exp(c)+ep0[a,b])/((1-ep1[a,b])*np.exp(c)+(1-ep0[a,b]))
    elif(a>b):
        w=(ep1[b,a]*np.exp(c)+ep0[b,a])/((1-ep1[b,a])*np.exp(c)+(1-ep0[b,a]))
    return np.log(w)
M={(1,2):0,(2,1):0,(2,3):0,(3,2):0,(3,5):0,(5,3):0,(2,4):0,(4,2):0,(3,6):0,(6,3):0}
eM={1:0,5:0,6:0}
B=np.zeros(7)
def bp(i): #Summing messages from neighbours
    x=0
    for k in range(7):
        if ((k,i) in M.keys()):
            x+=M[k,i]
    if i==1 or i==5 or i==6:    
        x+=eM[i]
    return x
def update():
    for i in range(1,7):    
        for j in range(1,7):
            if ((j,i) in M.keys()):
                if(j>i):
                    msg=B[j]-desc*M[i,j]
                    M[j,i]=wt(i,j,msg)
                if(i>j):
                    msg=B[j]-asc*M[i,j]
                    M[j,i]=wt(i,j,msg)
    for i in range(1,7):
        B[i]=bp(i)
 

for trial in range(1):
    eM[1]=-2
    eM[5]=eM[6]=1    #clamping messages for end nodes
    for g in range(20):  
        update()
        LOR.append(B[1:7])   #Skip 0 index
        
      
     
