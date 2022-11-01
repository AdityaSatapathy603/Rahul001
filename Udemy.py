#email_add = {"aditya": "adityasatapathy603@gmail.com", "michael": "michaelmaxx603@gmail.com", 
                #"shreya": "shreya14012004@gmail.com", "mom": "bharatisatapathy75@gmail.com", "dad": "umakantas20@gmail.com",
                #"vinay sir": "vinayblue@gmail.com", "avi": "avipatel15dec@gmail.com",
                #"chinese": "nibharai003@gmail.com", "vansh": "vansh0891@gmail.com", "priyanshi": "riddhisiddhi2600@gmail.com",
                #"himanshi": "himanshikumawat103@gmail.com", "kush": "pandyakush09@gmail.com", "mukesh sir": "mukeshshrimali14june@gmail.com",
                #"adityasharma":"adisharmamufc@gmail.com", "naisha": "naisha.jain31@gmail.com", "taha": "kagzi.taha@gmail.com",
                #"shrivastava": "shreyaashrivastava@gmail.com"}

#query = input("Name of repctian: ")
#print(email_add.pop(query))

#import random
#import pyttsx3
#data = pyttsx3.init()
#d = str(random.randrange(100, 1000, 2))
#data.say(d)
#data.runAndWait()

import matplotlib.pyplot as plt 
import numpy as np

u = [0, 56.1, 87.6, 116, 156, 234, 332, 432, 532, 632, 732, 1073, 2073]
v = [0, 0.439, 1.12, 1.84, 2.44, 2.66, 2.68, 2.68, 2.68, 2.68, 2.68, 2.68, 2.68,] 

w = [1.25, 44.3, 67.4, 84.6, 100, 116, 137, 171, 244, 342, 448, 1044, 2044]
x = [0, 0.557, 1.33, 2.15, 3, 3.84, 4.63, 5.29, 5.56, 5.58, 5.58, 5.58, 5.58]

y = [1.59, 37.7, 57.5, 71.6, 83.3, 94, 105, 116, 130, 148, 180, 1015, 2015]
z = [0, 0.623, 1.43, 2.28, 3.17, 4.06, 4.95, 5.84, 6.70, 7.52, 8.20, 8.51, 8.51]

plt.plot(u, v, 'r', label='IB = 10 μA')
plt.plot(w, x, 'g', label='IB = 20 μA')
plt.plot(y, z, 'c', label='IB = 30 μA')

plt.xlabel('VCE (mV)') 
plt.ylabel('IC (mA)') 

plt.title('IC vs VCE') 

plt.legend()
plt.grid()
plt.show()