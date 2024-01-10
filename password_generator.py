
import random
import string

print("Hey! lets generate a password")

#List of characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()abcdefghijklmnopqrstuvwxyz"
#Prompt the user to specified the length of the password
passwordLength = int(input("How long will you like your password to be ?"))
#Generate a random password
newPassword = []

for x in range(passwordLength):
    newPassword.append(range.choice(characters))
    
finalPassword = ''.join(map(str, newPassword))
