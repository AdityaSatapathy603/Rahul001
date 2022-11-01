import random
import pyautogui

chars = "abcdefghijklmnopqrstuvwxyz012345678!@#$%&*,./?\|_-"
chars_list = list(chars)

password = pyautogui.password("Enter a password ")

guess_password = ""
while(guess_password != password):
    guess_password = random.choices(chars_list , k=len(password))
    print("<"+ str(guess_password) +">")

    if (guess_password == list(password)):
        print("Your password is "+ "".join(guess_password))
        break
