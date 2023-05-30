#Task 5:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and determines the day of the week on which that date falls.
import datetime
s=input()
now=datetime.datetime.strptime(s, '%d-%m-%Y')
a=datetime.datetime.strftime(now,"%A")
print(a)