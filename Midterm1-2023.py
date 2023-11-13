#!/usr/bin/env python
# coding: utf-8

# # ACM20030 - Midterm 1 - 2023
# 
# This midterm exam starts at 5pm on Monday 13th of November and lasts **45 minutes**. Five additional minutes are given at the end for you to upload the Midterm1.ipynb to BrightSpace.
# 
# Save your notebook regularly as you are solving the problems.
# 
# I recommend you have a pen and paper handy to make small calculations (these do not need to be handed in).
# 
# The marks for each question are given in square brackets at the start of each question. The total marks for the test is 29.
# 
# You must complete the test indivudually. No contact with other class members, or anyone else, is allowed during the test.
# 
# You must complete the test indivudually. No contact with other class members, or anyone else, is allowed during the test. You are allowed to refer to the ACM20030-Examples notebooks (they must be saved on your laptop), your answers to previous assignments, and the lecture slides. You cannot view any other notebooks or files on your computer.
# 
# If there are any issues with uploading the midterm to BrightSpace please email me your completed Midterm1.ipynb immediately. My email address is niels.warburton@ucd.ie. Please include your student number if you email the test to me.
# 
# You **may not** use any other Python libraries other than NumPy and Matplotlib.  

# ## Checking you are in the exam room
# 
# Please enter the 4 digit number shown on the projector/board in the next cell

# In[1]:


1729


# ## Enter you student number

# In[2]:


# Enter student number below
# 21331176


# In[3]:


# Import NumPy and matplotlib
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


# The below two lines set the default size and font size for matplotlib
plt.rcParams['figure.figsize'] = (16.0, 10.0)
plt.rcParams.update({'font.size': 22})


# # Question 1: plotting
# 
# Plot the following functions. Take note of the required range and formatting.

# ## Q1a [3 marks]
# 
# Plot 
# 
# $$f(x) = x^4-2 x^3-7 x^2+8 x+12$$
# 
# in the range $x = -2.5\dots3.5$. 
# 
# Also:
# - Label both axes and put a grid on the plot. 
# - State, by visual inspection, the four values of $x$ for which $f(x) = 0$.

# In[6]:



def f(x):
    return x**4 - 2*x**3 - 7*x**2 + 8*x + 12

x_values = np.linspace(-2.5, 3.5, 100)

plt.plot(x_values, f(x_values), label='f(x)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # x-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # y-axis

# Labels
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

# roots
roots_x = [-2, -1, 1, 3]
roots_y = [f(x) for x in roots_x]
plt.scatter(roots_x, roots_y, color='red', label='Roots')

plt.legend()

plt.show()


# -2, -1 , 2 ,3
# 

# ## Q1b [4 marks]
# 
# We can define a spiral parametrically by
# 
# $$\begin{align}
#     x_1(t) &= t^{1/2} \cos(t)  \\
#     y_1(t) &= t^{1/2} \sin(t)
# \end{align}$$
# 
# We can also define a cardioid via
# 
# $$\begin{align}
#     x_2(t) &= 2a[1-\cos(t)]\cos(t)  \\
#     y_2(t) &= 2a[1-\cos(t)]\sin(t) 
# \end{align}$$
# 
# By letting $a=1.2$, plot both of these curves on the same plot with $t=0\dots4\pi$. Add a grid to the plot and a lengend showing 'spiral' and 'cardiod'

# In[7]:


def spiral(t):
    x = t**0.5 * np.cos(t)
    y = t**0.5 * np.sin(t)
    return x, y

def cardioid(t, a=1.2):
    x = 2*a*(1 - np.cos(t)) * np.cos(t)
    y = 2*a*(1 - np.cos(t)) * np.sin(t)
    return x, y

t_values = np.linspace(0, 4*np.pi, 100)

#curves
plt.plot(*spiral(t_values), label='Spiral')
plt.plot(*cardioid(t_values), label='Cardioid')


plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.legend()

plt.show()


# # Question 2: programming fundamentals
# 
# ## Q2a [3 marks]
# 
# The following code reverses the elements of an array and prints out the reversed array

# In[9]:


data = np.array([1,5,25,2,3,4,5,6]);

data = np.flip(data)

print(data)


# Using a while loop, write some code to reverse the data in the array without using `np.flip()` or any similar NumPy functions. Hint: it might help to note that the length of the array is even.

# In[11]:


data = np.array([1, 5, 25, 2, 3, 4, 5, 6])

i = 0
while i < len(data)//2:
    temp = data[i]
    data[i] = data[len(data)-1-i]
    data[len(data)-1-i] = temp
    i += 1
    
print(data)


# ## Q2b [3 marks]
# 
# By writing nested ``while`` loops (a loop within a loop) sum all the elements in the following $3\times3$ matrix (without using any special NumPy functions)

# In[13]:


A = np.array([[1.5,2.3,6.7,5.6],[-6.7,3.3,2.2,-9.9],[-4.5,0.1,2.9,-1.2],[4.5,0.4,-0.3,8.5]])
print(A)


# In[14]:


A = np.array([[1.5, 2.3, 6.7, 5.6], [-6.7, 3.3, 2.2, -9.9], [-4.5, 0.1, 2.9, -1.2], [4.5, 0.4, -0.3, 8.5]])

row = 0
total_sum = 0
while row < len(A):
    col = 0
    while col < len(A[row]):
        total_sum += A[row][col]
        col += 1
    row += 1

print(total_sum)


# using the calculator my result was 15.4

# ## Q2c [3 marks]
# 
# The golden ratio can be defined via the continued fraction:
# 
# $\phi=1+\cfrac{1}{1+\cfrac{1}{1+\cfrac{1}{ 1+\cfrac{1}{1+\cfrac{1}{1+\cfrac{1}{1+\cdots}}}}}}$
# 
# One way to calculate this is by repeated applying the function $f(n) = 1+1/n$ starting with $n=1$, i.e., $\phi = f(f(f(\dots f(f(1)))$. Define the function $f$ and using a `while` loop repeated apply $f$ to its own output 30 times. Compare your result to the true value for the golden ratio:
# 
# $$\phi = \frac{1+\sqrt{5}}{2}$$

# In[18]:


n = 30
Gr = 1.0
i = 1
while i <= n:
    Gr = 1 + 1 / phi
    i += 1

true_GR = (1 + 5**0.5) / 2
print("Calculated Gr:", Gr)
print("True Gr:", true_GR)


# my calculated golden ratio is almost exactly equal to the real golden ratio

# In[ ]:





# ## Q2d [4 marks]
# 
# 

# Let $g(x)$ be a piecewise function such that
# 
# $$g(x) = \begin{cases} 
#       -x & x\leq 0 \\
#       h(x) & 0\leq x\leq 1 \\
#       x-1 &  x \geq 1
#    \end{cases}$$
#    
# where $$h(x) = x(1-x)$$
# 
# Define the functions $h(x)$ and $g(x)$ and plot $g(x)$ over the range $x=-1\dots2$. Hint: to define $g$ you may wish to use ``if``, ``elif`` and/or ``else``

# In[19]:


def h(x):
    return x * (1 - x)

def g(x):
    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return h(x)
    else:
        return x - 1

x_values = np.linspace(-1, 2, 100)
plt.plot(x_values, [g(x) for x in x_values])

plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True)

plt.show()


# In[ ]:





# In[ ]:





# # Question 3: root finding
# 
# ## Q3a [4 marks]
# 
# Using the below `SecantMethod()` function, numerically find all the roots of $f(x) = 6\sin(x)-x^2 + 1$ to within an error $<10^{-6}$. 
# 
# Hints:
# 
# - It may help to plot the function to find good initial guesses.
# - Check the answers you find give $f(x_*)$ very near zero

# In[21]:


def SecantMethod(f, x0, x1, tol):
    i = 0
    xim1 = x0
    xi   = x1
    fi = 1
    while np.abs(fi) > tol:
        fi   = f(xi)
        xi1  = xi - fi*(xi - xim1)/(fi - f(xim1))
        xim1 = xi
        xi   = xi1
        
        i += 1

    return xi1


# In[29]:


def SecantMethod(f, x0, x1, tol):
    i = 0
    xim1 = x0
    xi = x1
    fi = 1
    while np.abs(fi) > tol:
        fi = f(xi)
        xi1 = xi - fi * (xi - xim1) / (fi - f(xim1))
        xim1 = xi
        xi = xi1
        i += 1
    return xi1
#my code

def f(x):
    return 6 * np.sin(x) - x**2 + 1

# Finding the roots using the Secant Method
root1 = SecantMethod(f, -1, 0, 1e-6)
root2 = SecantMethod(f, 1, 2, 1e-6)
root3 = SecantMethod(f, 3, 4, 1e-6)

print("Roots:", root1, root2, root3)


# In[ ]:





# In[ ]:





# ## Q3b [5 marks]
# 
# Use the below FindRootBisection method in this question -- note the function only works when $f(a) < 0 < f(b)$

# In[26]:


def FindRootBisection(f, a, b, tol):
    left = a
    right = b
    while right-left > tol:
        midpoint = (left+right)/2
        if(f(midpoint) < 0):
            left = midpoint
        else:
            right = midpoint
    return midpoint


# Use the bisection method on the function
# 
# $$f(x) = \frac{x^3-x-3}{(x-1) (x+2)}$$
# 
# with $a=-3$, $b=-1.1$ and $\text{tol}=10^{-12}$.

# In[38]:


def FindRootBisection(f, a, b, tol):
    left = a
    right = b
    while right - left > tol:
        midpoint = (left + right) / 2
        if f(midpoint) < 0:
            left = midpoint
        else:
            right = midpoint
    return midpoint
#my code

def f(x):
    return (x**3 - x - 3)/(x - 1)*(x + 2)

root = FindRootBisection(f, -3, -1.1, 1e-12)
print("root of f(x):", root)

x_values = np.linspace(-3, -1.1, 100)
plt.plot(x_values, f(x_values))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend("f(x)")
plt.show()


# In[ ]:





# Has the code found a root of $f(x)$? Provide one sentence to justify your answer.

# no, -2 would be a root if we look at the denominator (x+2), -1.99999999 is not quite a root, close though

# By plotting the function, bracket the true root and use the bisection method to find it's value to within an error of $<10^{-10}$. Check the answer you find is a root by substituting it back into $f(x)$.
# 
# Hint: you may find it useful to restrict the y-range of the plot to be from $-10\dots10$

# In[55]:


x = np.linspace(-10,10,100)
plt.plot(x,f(x))
plt.grid(True)
root = FindRootBisection(f,-3,-1.1,1e-10)
print(root)
print(f(root))
print('real roots of f(x)')


# slightly off again but basically -2!

# # Submission
# 
# You must upload your completed `Midterm1.ipynb` to BrightSpace. You can find the place to upload the file under the Assessments Tab -> Midterm1. I also recommend you commit and push your midterm to your GitHub repository.
# 
# If there are any issues with uploading the midterm to BrightSpace. Please email me your completed Midterm1.ipynb. My email address is niels.warburton@ucd.ie. 
