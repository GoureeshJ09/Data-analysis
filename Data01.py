#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


sales = pd.read_csv("D:/Data_analysis/sales_data.csv")


# In[3]:


sales.head()


# In[4]:


sales.shape


# In[5]:


sales.info()


# In[6]:


sales.describe()


# In[8]:


sales['Unit_Cost'].describe()


# In[10]:


sales['Unit_Cost'].mean()


# In[16]:


sales['Unit_Cost'].plot(kind='box', vert=False, figsize = (15,6))


# In[17]:


sales['Unit_Cost'].plot(kind='density', figsize=(15,6))


# In[23]:


ax = sales['Unit_Cost'].plot(kind='density', figsize=(15,6))
ax.axvline(sales['Unit_Cost'].mean(),color='red')
ax.axvline(sales['Unit_Cost'].median(),color='green')


# # Categorical analysis and visualization

# In[26]:


sales.head()


# In[28]:


sales['Age_Group'].value_counts()


# In[33]:


sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))


# # Relationship between the columns

# ## Study of correlation

# In[34]:


corr = sales.corr()


# In[35]:


corr


# In[40]:


fig = plt.figure(figsize=(5,5))
plt.matshow(corr, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical');
plt.yticks(range(len(corr.columns)), corr.columns);


# In[42]:


sales.plot(kind='scatter', x = 'Revenue', y = 'Profit', figsize = (5,5))


# In[43]:


ax = sales[['Profit','Age_Group']].boxplot(by='Age_Group', figsize=(8,8))
ax.set_ylabel('Profit')


# # Column wrangling

# In[44]:


sales.head()


# In[45]:


sales["Revenue_per_Age"] = sales['Revenue']/sales['Customer_Age']


# In[46]:


sales['Revenue_per_Age'].head()


# In[51]:


ab = sales['Revenue_per_Age'].plot(kind='density', figsize = (5,5))
ab.axvline(sales['Unit_Cost'].median(),color='red')


# In[54]:


sales['Revenue_per_Age'].plot(kind='hist', figsize = (5,5))


# In[56]:


sales['Revenue_per_Age'].describe()


# In[57]:


sales.head()


# In[58]:


sales['Calculated_cost'] = sales['Order_Quantity']*sales['Unit_Cost']
sales['Calculated_cost']


# In[59]:


sales['Calculated_cost'].shape


# In[60]:


(sales['Calculated_cost']!=sales['Cost']).sum()


# In[61]:


sales.plot(kind='scatter', x = 'Calculated_cost', y = 'Profit', figsize=(5,5))


# # Selection and Indexing

# In[62]:


sales.head()


# In[65]:


sales.loc[sales['State'] == 'Kentucky']


# In[ ]:




