import matplotlib.pyplot as plt
import numpy as np

labels = 'Python', 'C++', 'R', 'Java'
sizes = [245, 130, 215, 210]
colors = ['gold', 'green', 'orange', 'lightskyblue']
explode = (0.1, 0.3, 0, 0)  # explode 1st slice

# Plot
plt.subplot(2,1,1)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=0)



# x axis values 
x = [100, 110, 96, 155, 130, 145, 169]
# corresponding y axis values 
y = [137, 67, 99, 105, 129, 146, 150]

# plotting the points
plt.subplot(2,1,2) 
plt.bar(x, y) 

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 

# giving a title to my graph 
plt.title('graph') 

# function to show the plot 
plt.show()