#!/usr/bin/env python
# coding: utf-8

# # Visualizing my LinkedIn Network

# In[9]:


import pandas as pd
import plotly.express as px
import numpy as np


# ### Import data

# In[10]:


df = pd.read_csv('LinkedIn_Connections.csv')
df = df.drop(['Email Address'], axis=1)
df.to_csv('LinkedIn_Connection.csv')
