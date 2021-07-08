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
df = df.dropna(subset=['Company', 'Position'])


# In[11]:


# create root node for treemap
df['My Network'] = 'My Network'
# group company synonyms
df.loc[df['Company'] == 'XING', 'Company'] = 'XING'


# In[12]:


pos_count_series = df.groupby(['Position'])[['First Name']].count()

def get_position_count(position):
    return pos_count_series['First Name'].loc[position]

df['Position Count'] = df['Position'].apply(lambda x: get_position_count(x))
df


# In[13]:


df.to_csv('output.csv')


# ## Treemap on Company

# In[22]:


fig = px.treemap(df, path=['My Network', 'Company', 'Position'], width=1000, height=1000)
fig.show()


# ## Treemap on Position

# In[25]:


fig = px.treemap(df, path=['My Network', 'Position', 'Company'], width=1000, height=1000)
fig.show()


# In[8]:


fig = px.sunburst(df, path=['My Network', 'Company', 'Position'], width=1000, height=1000)
fig.show()


# In[9]:


fig = px.sunburst(df, path=['My Network', 'Position', 'Company'], width=1000, height=1000)
fig.show()


# In[14]:



fig = px.scatter(df, x="Relation", y="Position Count",
	         size="Relation", color="Relation",
                 hover_name="Position", log_x=True, size_max=60)
fig.show()


# In[ ]:




