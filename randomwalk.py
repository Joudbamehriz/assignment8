# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:39:16 2024

@author: joahb
"""

import random as rd
import matplotlib.pyplot as plt
import statistics


displacement=[]
displacementtot=[]
n= int(input("enter the number of step:"))
for walker in range (0,500):
    startpos= 0 
    steps=[]
    numbersteps=[]
    displacementsq=[]
    for i in range (0,n): 
       newpos=startpos+rd.randint(-1,1) 
       steps.append(newpos)
       startpos=newpos
       displacementsq1=(steps[i]-steps[0])**2
       displacementsq.append(displacementsq1)
       numbersteps.append(i)
       i = i+1
       plt.plot(numbersteps, steps, label="position")
    displacement1=steps[n-1]-steps[0]
    displacement.append(displacement1)
    displacementtot.append(displacementsq)

mean_displacement_sq = [0] * n  
for step_idx in range(n):
    step_sum = 0
    for walker in range(500):  
        step_sum += displacementtot[walker][step_idx]
    mean_displacement_sq[step_idx] = step_sum / 500

# Plot the mean squared displacement as a function of step number
plt.plot(range(n), mean_displacement_sq, label="Mean Squared Displacement")

  
plt.xlabel("step number")
plt.ylabel("position/displacement")
plt.title("position/displacement vs step number")
#plt.ylabel("position")
#plt.title("position vs step number")
plt.grid(True)
#plt.legend()
plt.show()


print("the mean displacement is:", statistics.mean(displacement))
print("the mean displacement squared is:", statistics.mean(displacementsq))


   
   
   
