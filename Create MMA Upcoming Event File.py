#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[5]:


Upcoming_Fighter_List = pd.read_excel('C:/Users/schne/Desktop/MMA Prediction Files/UpcomingFightList.xlsx')
Fights_File=pd.read_excel('C:/Users/schne/Desktop/MMA Prediction Files/UseforViz.xlsx')


# In[12]:


# UFL=Upcoming_Fighter_List['Winners'].to_list()
Fights_File.columns


# In[29]:


Fight_To_Use = list()
Temp=Fights_File.sort_values(by ='Date', ascending = False)
for Fighter in UFL:
    Fight_To_Use.append((Temp[Temp['NAME_A']==Fighter][:1].mean()))
    print(len(Temp[Temp['NAME_A']==Fighter]))
    print(Fighter)
    

# Fights_File


# In[30]:


Fight_To_Use


# In[34]:


mean_matrix = pd.concat(Fight_To_Use, axis=1).T
mean_matrix


# In[36]:


mean_matrix.to_excel('C:/Users/schne/Desktop/MMA Prediction Files/Upcoming.xlsx')

