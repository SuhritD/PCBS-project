# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:17:18 2019

@author: Suhrit
"""''
import numpy as np, matplotlib.pyplot as plt
prob0={(1,2):0.1,(2,3):0.1,(3,5):0.1,(2,4):0.1,(3,6):0.1}
prob1={(1,2):0.9,(2,3):0.9,(3,5):0.9,(2,4):0.9,(3,6):0.9}
state=np.zeros(7)
asc=desc=1 #Inhibition of loops 
def wt(a,b,c): #weights of the messages
    if(b>a):
      w=(prob1[a,b]*np.exp(c)+prob0[a,b])/((1-prob1[a,b])*np.exp(c)+(1-prob0[a,b]))
    elif(a>b):
        w=(prob1[b,a]*np.exp(c)+prob0[b,a])/((1-prob1[b,a])*np.exp(c)+(1-prob0[b,a]))
    return np.log(w)
Message={(1,2):0,(2,1):0,(2,3):0,(3,2):0,(3,5):0,(5,3):0,(2,4):0,(4,2):0,(3,6):0,(6,3):0}
extMessage={1:0,5:0,6:0}
Belief=np.zeros(7)
def bp(i): #Summing messages from neighbours
    x=0
    for k in range(7):
        if ((k,i) in Message.keys()):
            x+=Message[k,i]
    if i==1 or i==5 or i==6:    
        x+=extMessage[i]
    return x
def update(B):
    for i in range(1,7):    
        for j in range(1,7):
            if ((j,i) in Message.keys()):
                if(j>i):
                    msg=B[j]-desc*Message[i,j]
                    Message[j,i]=wt(i,j,msg)
                if(i>j):
                    msg=B[j]-asc*Message[i,j]
                    Message[j,i]=wt(i,j,msg)
    for i in range(1,7):
        B[i]=bp(i)
    return B
 
Belief=np.zeros(7)
LOR=np.zeros((20,6))
#set clamping messages for end nodes
extMessage[1]=-2
extMessage[5]=extMessage[6]=1    
for trial in range(20):
    update(Belief)
    print(Belief)
    LOR[trial]=(Belief[1:7])
        
      
     
