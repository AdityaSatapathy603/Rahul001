#import pywhatkit as kit
#src_path = 'OIP.jfif'
#convey = kit.image_to_ascii_art(src_path)
#print(convey)

import matplotlib.pyplot as plt
week = [1,2,3,4,5]
shift1 = [40, 35, 26, 32, 23]
shift2 = [40, 32, 40, 45, 50]
shift3 = [40, 35, 45, 42, 40]

plt.stackplot(week, shift1, shift2, shift3, labels=['shift1','shift2','shift3'])
plt.legend()
plt.show()