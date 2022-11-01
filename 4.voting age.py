#program that determine whether you are eligible to vote in terms of age input
# Name input command line defined as variable X
X = input(str("Enter your Name = "))

# Age input command line defined as variable Y
Y = input(int("Enter your Age = "))

# 'if' conditional statement
if (Y>=18):
    print(X,", you are eligible to cast vote. Go ahead") #output line if candidate is 18 yrs or above

else:
    print(X,", you are under-aged. You cannot cast vote.") #output line if candidate is less than 18 yrs
