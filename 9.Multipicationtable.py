# Multipication table in any range from 1
# number input command line for the number whose table you want to print defined as num
num = int(input("Enter number whose multiplication table is to be displayed : "))

# defining a range for the output of the input number-table to be printed
for z in range (1,11): #defining a variable for range
# note : if you want to select a range from 1 to 10; input range 1 to 11.
# The compiler will not take into account the last number defined as end range i.e. 11 in this case.
# It take -1 of the number input as end range
    print(num,"x",z,"=", num*z)
    # the claculation part of the multipicative table is done in the print statement itself i.e.(num*z)
