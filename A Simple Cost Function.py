#!/usr/bin/env python
# coding: utf-8

# 

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# ## Simple Cost function
# $$ f(x) = x^2 + 4x + 5 $$

# In[6]:


# 
def f(x):
    return x**2 + 4*x + 5


# In[9]:


x_1 = np.linspace(-3,3,20)


# In[12]:


# Plotting our func in the graph
plt.plot(x_1,f(x_1))
plt.show()


# ### Derivative or slope of our function

# In[13]:


def df(x):
    return 2*x + 4


# In[15]:


# Plotting our Graph and Slope side by side

plt.figure(figsize=[10,5])

# Chart 1 : Function f(x)

plt.subplot(1,2,2)
plt.plot(x_1,f(x_1))

# Chart 2 : Slope of Function f(x)

plt.plot(x_1,df(x_1))


plt.show()


# In[ ]:




