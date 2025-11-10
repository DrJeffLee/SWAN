# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 10:01:49 2025

@author: 40423339
"""

import numpy as np
import matplotlib.pyplot as plt

data= np.genfromtxt(r"C:\Users\40423339\Desktop\SWAN Bathymetry\March28\full_domain_table.dat" , skip_header=7)
data_mask=data.copy()
data[data_mask<0]=np.NaN
Hs=data[:,0].reshape((241,337))
Tp=data[:,1].reshape((241,337))
depth=data[:,2].reshape((241,337))
TANK_LENGTH = 16.8  # m
TANK_WIDTH = 12.0   # m


# 2D Bathymetry Contour Plot
plt.imshow(Hs, aspect='auto', cmap='viridis', 
           extent=[0, TANK_LENGTH, 0, TANK_WIDTH])  # Origin at bottom-left
#plt.clim(0,0.05)
plt.colorbar(label='Hs (m)')
plt.title('Wave height (m)')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.show()

plt.imshow(Tp, aspect='auto', cmap='viridis', 
           extent=[0, TANK_LENGTH, 0, TANK_WIDTH])  # Origin at bottom-left
#plt.clim(0,2)
plt.colorbar(label='Tp (s)')
plt.title('Wave period (s)')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.show()

plt.imshow(depth, aspect='auto', cmap='viridis', 
           extent=[0, TANK_LENGTH, 0, TANK_WIDTH])  # Origin at bottom-left
plt.clim(0,0.5)
plt.colorbar(label='depth (m)')
plt.title('depth (m)')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')

plt.show()



