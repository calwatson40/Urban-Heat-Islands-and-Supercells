# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python
# coding: utf-8

# # Title
# The purpose of this Jupyter Notebook is to demonstrate how . . .
#
# ## Where did the data come from?
# The data were downloaded from the NOAA National Center for Environmental Information. - - - EDIT THIS!
# Details about the database and the data files are available here:
# https://www.ncdc.noaa.gov/stormevents/details.jsp
#
# ## What Files are there
# * 
# In[1]:


# Imports
import numpy as np
import pandas as pd


# In[2]:


# Filename
fname=r"C:\Users\calwa\OneDrive - University of Oklahoma\Shared Folder\Desktop\OU\2022-23\Spring\METR 3334\Reflectivity_Values.csv"

# Read in the data using pandas
base_rf = pd.read_csv(fname)

# Create column names
time = base_rf['July 2, 2008 (Time (Z))']
reflectivity = base_rf['dB']

# Make a line chart using matplotlib
import matplotlib.pyplot as plt
plt.figure(figsize=(11,6))
plt.plot(time, reflectivity, '-o', label='Reflectivity (dB)', color='navy')
plt.legend(bbox_to_anchor=(1.01,0.54))
plt.title('0.5 Degree Elevation Scan Maximum Reflectivity Values (in dB) for a \n Thunderstorm that Moved through Omaha' + "'s" + ' UHI', fontweight='bold')

# X-axis
plt.xticks(rotation=45,ha='right',fontsize=8)
plt.xlabel('July 2, 2008 (Time (Z))', fontweight='bold')

# Y-axis
plt.ylim([0,80])
plt.ylabel('dB', fontweight='bold')

# Add horizontal lines
plt.grid(axis='y', color='black')

# Set background color to gray
ax = plt.gca()
ax.set_facecolor((0.65,0.65,0.65))




