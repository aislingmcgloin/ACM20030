#!/usr/bin/env python
# coding: utf-8

# ## question 1

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# 

# In[2]:


import numpy as np
def VectorLength(x, y):
    v = np.sqrt(x*x + y*y)
    return v



# In[3]:


print(VectorLength(5,6))


# In[4]:


print(VectorLength(-1,5))


# In[5]:


r = np.sin(1)
y = np.round(r, 3)
print(y)
print("sin(1) =" , y)


# ## Question 2

# In[6]:


# function to check if a number is prime
def IsPrime(n):
    i = 2
    while i < np.sqrt(n):
        # For each i check if it divides n
        if(n % i ==0):
            return 0
        i += 1
        # if no divisors are found, the number is prime
    return 1
        


# In[7]:


print(IsPrime(1))


# In[8]:


print(IsPrime(2))


# In[9]:


print(IsPrime(3))


# In[10]:


print(IsPrime(4))


# In[11]:


print(IsPrime(5))


# In[12]:


print(IsPrime(6))


# In[13]:


print(IsPrime(7))


# In[14]:


print(IsPrime(8))


# In[15]:


print(IsPrime(9))


# In[16]:


print(IsPrime(10))


# it does not accuratley check if a number is prime as 2 and 3 are prime, it also returns that 9 is prime and its not.

# In[17]:


# function to check if a number is prime
def IsPrime1(n):
    if n == 1:
        return 0
    i = 2
    while i <= np.sqrt(n):
        # For each i check if it divides n
        if(n % i ==0):
            return 0
        i += 1
        # if no divisors are found, the number is prime
    return 1


# In[18]:


print(IsPrime1(1))


# In[19]:


print(IsPrime1(4))


# In[31]:


print(IsPrime1(9))


# I added a case to fix it

# In[20]:


def countprime(n):
    i = 1
    count = 0
    while i < n:
        if IsPrime1(i) == 1:
            count = count + 1
        i = i+ 1 
    return count 

        


# In[21]:


countprime(10)


# In[22]:


countprime(1000)


# # question 2G

# In[23]:


x = np.arange(0,40,1)
Pi = np.zeros(40)
i=0
while i < np.size(Pi):
    Pi[i] = countprime(i)
    i += 1


# In[24]:


plt.plot(x, Pi, 'ro')
plt.xlabel("x")
plt.ylabel("Pi(x)")
plt.grid(True)


# ## Question 3

# In[25]:


data = np.loadtxt("PowerLawOrExponential (4).txt")


# In[26]:


xdata = data[:,0]
xdata


# In[27]:


ydata = data[:,1]
ydata


# In[28]:


plt.plot((xdata), np.log(ydata))
plt.grid(True)
plt.title("log plot")
plt.xlabel("X")
plt.ylabel("Y")


# In[29]:


plt.plot(np.log(xdata), np.log(ydata))
plt.grid(True)
plt.title("log plot")
plt.xlabel("X")
plt.ylabel("Y")


# yes, the data is discrete 

# In[30]:


n=4/2


# In[ ]:





# In[ ]:




