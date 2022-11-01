# import libraries
import matplotlib.pyplot as plt

# create labels or text for the chart reference
labels = 'Python', 'C++', 'R', 'Java'

# size or value of each label
sizes = [245, 130, 215, 210]

# color imparted to each section/label to distinguish
colors = ['gold', 'green', 'orange', 'lightskyblue']

# to make the section with largest value stand out
explode = (0.1, 0, 0, 0)  # explode 1st slice correspondence of  value

plt.pie(sizes, explode=True, labels=labels,
colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)
#this is to confirm what fields are to be shown in final plot
# for eg: if you mentioned colors but to not want to make them
# visible in final plot do not mention color in plt.pie
# startangle refers to at what angle the pie graph should start plotting
#autopct is presicion to which the plotting will be done

plt.title("Pie Graph for languages users in thousands")
# Title to the graph to which the graph is about

plt.show()# A type of print statement to display the pie chart