#program to get Simple Interest of an amount on any rate-of-interest at any time
#  get principle amt input from user on which Simple Interest is to be found out
# Principle Amount input command line defined as variable P
P = float(input("Enter Principle Amount = ")) #Using float datatype will help user to input accurate value

#  get Rate-of-Interest input from user 
# Rate-of-Interest input command line defined as variable R
R = float(input("Enter Rate-of-Interest = ")) #Using float datatype will help user to input accurate value

#  get Time period input from user over which S.I. is to be calculated
# Time Period input command line defined as variable T
T = float(input("Enter Time Period = ")) #Using float datatype will help user to input accurate value

#formula to claculate the S.I.
SI = float(P*R*T/100) #Using float datatype will give user an accurate and presize value of their S.I.

#output Command line
print("Your calculated Simple Interest is ",SI)