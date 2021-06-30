#!/usr/bin/env python
# coding: utf-8

# 피클로 담은 변수를 다시 가져오기

# In[1]:


import pickle


# In[3]:


pickle.load(open('./saves/favorite_save.pkl','rb'))


# In[6]:


favorite_load=pickle.load(open('./saves/favorite_save.pkl','rb'))
print(favorite_load)


# In[7]:


print(favorite_load['tiger'])


# In[9]:


pickle.load(open('./saves/autompg_lr.pkl','rb'))


# In[11]:


autompg_lr=pickle.load(open('./saves/autompg_lr.pkl','rb'))
print(autompg_lr,type(autompg_lr))


# In[12]:

#input from outside
#print(autompg_lr.predict([[3504.0,8]])) 와 아래가 같음
a= 3504.0
b= 8

import numpy as np
pre=np.array([[a,b]])
print(autompg_lr.predict(pre))

# In[ ]:




