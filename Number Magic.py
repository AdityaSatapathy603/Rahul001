print("Hello, Think of a number of your choice.")
#one = str(input("Do you have the number in mind yet.(y/n)..."))

while True:
    #count1 = 0
    one = str(input("Do you have the number in mind yet.(y/n)..."))
    if 'y' in one or 'Y' in one:
        print("Great!")
        break
    else:
        #count1 = count1 + 1
        print("Well, what are you waiting for...")
        continue
        

while True:
    two = str(input("Now substract 1 from the number you have in your mind.(y/n)..."))
    if 'y' in one or 'Y' in two:
        print("Good")
        break
    else:
        print("well go on then...we don\'t have the whole day!")
        continue
