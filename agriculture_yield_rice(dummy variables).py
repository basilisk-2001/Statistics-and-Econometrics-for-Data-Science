#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd


# In[32]:


import numpy as np


# In[33]:


df=pd.read_csv("Dataset.csv")


# In[34]:


df


# In[35]:


df1=pd.get_dummies(df['Irrigation'])
df2=pd.concat([df1,df],axis=1)


# In[36]:


df2


# In[ ]:




