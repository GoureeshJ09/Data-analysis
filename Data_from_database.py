#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd


# In[27]:


certificates_earned = pd.DataFrame({
    'Certificates': [8,2,5,6],
    'Time': [16,5,9,12]
})

names = ['tom','kris','ahmad','beau']
certificates_earned.index = names
longest_streak = pd.Series([13,11,9,7], index = names)
certificates_earned['Longest streak'] = longest_streak
print(certificates_earned)


# # Pandas - Series

# In[28]:


import numpy as np


# In[29]:


import numpy as np


# In[30]:


g7_pop = pd.Series([35.467, 63.931, 80.958, 60.665, 85.225,90.555,127.000])


# In[31]:


g7_pop


# In[33]:


g7_pop.name = 'G7 population in millions'


# In[34]:


g7_pop


# In[37]:


g7_pop.describe()


# In[38]:


g7_pop.head()


# In[39]:


g7_pop.values


# In[40]:


g7_pop.index


# In[42]:


g7_pop.index = ['Canada','France','Germany','Italy','Japan','UK','The USA']


# In[43]:


g7_pop


# In[44]:


g7_pop


# In[45]:


g7_pop['Canada']


# In[47]:


g7_pop.iloc[0]


# In[48]:


g7_pop.mean()


# In[50]:


g7_pop.plot(kind='pie', figsize=(5,5))


# In[53]:


g7_pop.plot(kind='density', figsize = (5,5))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




