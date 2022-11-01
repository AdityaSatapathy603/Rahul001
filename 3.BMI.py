#using height and weight data of an  person calculate the Body Mass Index of the indivisual 

# Enter the height of the person in meters
Height = float(input("Enter height in meters: ")) #user may change the height to inches accordingly

# 1 foot=12 inches so height of 5feet6inch person = (5 X 12)+ 6 = 66inches

# Enter the weight of the person in Kgs
Weight = float(input("Enter weight in Kilogram: ")) #user may change the weight to lbs according to convinience

# 1 kg = 2.204 lbs so 55kg = (55 X 2.204) = 121.254 lbs

# Formula to calculate Body Mass Index using User given data
BMI  = Weight/(Height**2)
# Formula for BMI calculator in inch-pound is :  [weight (lb) / height (in) / height (in)] x 703
#i.e. BMI = [Weight/Height/Height]*703

# "if" Conditional statement 

# creating BMI ranges to compare with output
if(BMI<16):
  print("Severly Underweight") #printing status of result if BMI is in range(<16)

elif(BMI>=16 and BMI<18.5):
  print("Underweight") #printing status of result if BMI is in range(>=16 & <18.5)

elif(BMI>=18.5 and BMI<25):
  print("Healthy") #printing status of result if BMI is in range(>=18.5 & <25)

elif(BMI>=25 and BMI<30):
  print("Overweight") #printing status of result if BMI is in range(>=25 & <30)

else:
  print("Severly Overweight") #printing status of result if BMI is in range(>30)

