#program to find whether or not two numbers on dividing have a modulator(remainder)
#simple dividing program to find that if there is a remainder on dividing two numbers

#user input value for 'divident' or also known as 'value to be modulated'
#divident/value to be modulated is defined or taken as variable x
x = int(input("Enter value of the digit to be modulated : "))#replacing int(integer) with float(decimal) will help to do complex decimal value calculation

#user input value for 'divisior' 
#divisior is defined or taken as variable y
y = int(input("Enter value of modulator : "))#replacing int(integer) with float(decimal) will help to do complex decimal value calculation

#formula to find out remainder also known as modulator 
cal = int(x%y)##replacing int(integer) with float(decimal) will give user more accurate output

#printing the calculated modulator
print("Modulator of the given value is : " ,cal)