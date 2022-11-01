#Calculating the Volume of Cube or Cuboid
#Volume of cube or cuboid calculated by input of 3 dimensional measurments

# Length input command line defined as variable L
L = float(input("Enter Length : "))

# Breadth input command line defined as variable B
B = float(input("Enter Breadth : "))

# Height input command line defined as variable H
H = float(input("Enter Height : "))

# calculating volume using user inputs by formula for Cube/Cuboid Volume
Vol = float(L*B*H)

# 'if' conditional statement
if L==B==H:
    print("Volume of the Cube is ",Vol) #output Command line in case of cube

else:
    print("Volume of the Cuboid is ",Vol) #output Command line in case of cuboid
