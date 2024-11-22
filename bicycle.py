# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:03:11 2024

@author: joahb
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
v0 = 4.0       # initial velocity in m/s
m = 70.0       # mass of the cyclist in kg
P = 400.0      # power output in watts
dt = 0.1       # time step in seconds
t_max = 200.0  # total simulation time in seconds
C_d= 0.9       #aerodynamic drag coefficient 
A= 0.33        #cross sectional area of rider and bike
density= 1.225 #density of air at sea level
n = 2*10**(-5) #viscosity of air 
h = 2          #height
g = 9.81       #acceleration of gravity 

# Time array and velocity array
t = np.arange(0, t_max + dt, dt)
v = np.zeros_like(t)
v[0] = v0  # initial velocity


# Euler method to solve the equation dv/dt = P / (m * v)
for i in range(1, len(t)):
    dv_dt = P / (m * v[i - 1])
    v[i] = v[i - 1] + dv_dt * dt
v1 = v.copy() 

# Euler method to solve the equation dv/dt = P / (m * v) - F_drag(aero)/m
for i in range(1, len(t)):
    dv_dt = P / (m * v[i - 1])- ((1/2)*C_d*A*density*(v[i-1])**2)/m
    v[i] = v[i - 1] + dv_dt * dt
v2 = v.copy()

# Euler method to solve the equation dv/dt = P / (m * v) - F_drag(aero)/m - F_drag(viscous)/m
for i in range(1, len(t)):
    dv_dt = P / (m * v[i - 1])- ((1/2)*C_d*A*density*(v[i-1])**2)/m -(( n*A*(v[i-1]))/h)/m
    v[i] = v[i - 1] + dv_dt * dt
v3 = v.copy()
theta=np.arctan(int(input('enter the grade percentage:'))/100)

# Euler method to solve the equation dv/dt = P / (m * v) - F_drag(aero)/m - F_drag(viscous)/m -F_gravity/m
for i in range(1, len(t)):
    dv_dt = P / (m * v[i - 1])- ((1/2)*C_d*A*density*(v[i-1])**2)/m -(( n*A*(v[i-1]))/h)/m - g*np.sin(theta)
    v[i] = v[i - 1] + dv_dt * dt
v4 = v.copy()
    
# Plot the velocity over time
plt.figure(figsize=(10, 6))
plt.plot(t, v1, label="Velocity of Cyclist - no drag", color="blue")
plt.plot(t,v2, label="Velocity of Cyclist - aero drag", color="red")
plt.plot(t,v3, "m--", label="Velocity of Cyclist - aero +viscous drag")
plt.plot(t,v4, "g--", label="Velocity of Cyclist - aero +viscous drag + gravity")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity of a Cyclist Without Drag Over Time")
plt.legend()
plt.grid(True)
plt.savefig("bicycle_velocity.png")
plt.show()