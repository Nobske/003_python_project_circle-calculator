
# coding: utf-8

# In[ ]:


import numpy as np
pi = np.pi
radius = int(input("Please put in your radius from your circle: "))
def diameter(x):
    return 2*radius
def area(x):
    return pi*radius*radius
def circumference(x):
    return pi* diameter(x)
print("You put in the radius of {}, the diameter is {}, the area is {} and the circumference is {}".format(radius, diameter(radius), area(radius), circumference(diameter(radius))))
close = input("Press any button to close")

