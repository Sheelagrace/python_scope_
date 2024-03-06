#!/usr/bin/env python
# coding: utf-8

# In[1]:


def myfunc():
    x=100
    print(x)
    
myfunc()    
    


# ### what is meant by scope?
# #### A variable is only available from inside the region it is created

# In[4]:


x=100

def myfunc():

    print(x)
   
myfunc()

print(x)
   


# In[7]:


x=200

def myfunc():
    x=300
    print(x)
   
myfunc()

print(x)


# In[9]:


def myfunc():
    global x
    x=300
myfunc()
print(x)   


# ### Global?
# #### Variable out of function

# In[ ]:




