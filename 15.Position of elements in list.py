def check_list(n):
    defined_list = list(range(0, 100, 2))
    if n in defined_list:
        index = defined_list.index(n)
        print( " %s is in the range of list"%str(n))
        print("The position of the number is ",index," in the list.")
    else :
        print("The number is outside the given range.")
        
#print("this is your pre-defined list___")
#print(list(range(0, 100, 2)))
num = int(input("Enter a number: "))
check_list(num)
