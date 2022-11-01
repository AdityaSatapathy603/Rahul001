#programs to convert temperatures into different units

# temperature unit input command line is defined as 'query'
while True:
    query = str(input("Enter input temperature unit(f/c/k) : "))

# if conditional statement
    if 'f' in query:
    #if 'f' variable is in query, fahrenheit magnitude input command line defined as variable m will pop-up
        m = float(input("Enter magnitude of fahrenheit Temp = "))

        n = float(m-32)*(5/9) #formula to convert °F to °C defined as variable n
        o = float(m+459.67)*(5/9) #formula to convert °F to °K is defined as variable o
        print(m,"°F is ",n,"°Celsius and ",o,"Kelvin.") # output line for °F converted to °C & °K

    elif 'c' in query:
    #if 'c' variable is in query, celsius magnitude input command line defined as variable a will pop-up
        a = float(input("Enter magnitude of celsius Temp = "))

        b = float((a*9/5)+32) #formula to convert °C to °F defined as variable b
        c = float(a+273.15) #formula to convert °C to °K defined as variable c
        print(a,'°C is ',b,'°Fahrenheit and ',c,'Kelvin.') # output line for °C converted to °F & °K

    elif 'k' in query:
    #if 'k' variable is in query, kelvin magnitude input command line defined as variable a will pop-up
        x = float(input("Enter magnitude of kelvin Temp = "))

        y = float((x*9/5)-459.67) #formula to convert °K to °F defined as variable c
        z = float(x-273.15) #formula to convert °K to °C defined as variable c
        print(x,'K is ',y,'°Fahrenheit and ',z,'°Celsius.') # output line for °K converted to °F & °C

    else:
    # if other variable is in query, Input Error Command Line will display
        print("Invalid Temperature Unit Input!")

#Note : This temperature conversion calculator is only for 3 basic units of temperature 
#       you may enter more units ny following  the steps used to made the above calculator by using the 
#       correct formula for the conversion.
