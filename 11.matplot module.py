# importing the required module 
import matplotlib.pyplot as plt 
import numpy as np

# x axis values 
x = np.arange(0,4*np.pi,0.1) 
w = np.arange(0,np.pi*2,0.05)
# corresponding y axis values 
y = np.sin(x)
z = np.cos(x)
v = np.tan(x)

# plotting the points 
plt.plot(x, y,x,z,w,v) 

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 

# giving a title to my graph 
plt.title('sin graph') 

# function to show the plot 
plt.show()
