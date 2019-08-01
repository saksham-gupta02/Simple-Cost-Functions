#!/usr/bin/env python
# coding: utf-8

# ### Making a Gradient descent function as a module.
# 
# ### So that no need to write a function everytime we need our Gradient descent function.
# 
# ### Just save this in the same folder where your code is as .py 
# 

# In[1]:


def gradient_descent(derivative_func,initial_guess,multiplier = 0.02,precision = 0.001,max_iter = 300):
    new_x = initial_guess
    x_list = [new_x]
    slope_list = [derivative_func(new_x)]
    
    for n in range(max_iter):
        previous_x = new_x
        gradient = derivative_func(previous_x)
        new_x = previous_x - gradient * multiplier
        
        step_size = abs(new_x - previous_x)
        x_list.append(new_x)
        slope_list.append(derivative_func(new_x))
        
        if(step_size < precision):
            break
        
    return new_x,x_list,slope_list # Returning values as Tuples


# In[ ]:




