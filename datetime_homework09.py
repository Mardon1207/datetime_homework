#Task 9:
#Write a Python program that calculates the difference between two given dates. Prompt the user to enter two dates in the format "dd-mm-yyyy" and display the number of days between them.
import datetime
s=input()
now=datetime.datetime.strptime(s, '%d-%m-%Y')
a=input()
age=datetime.datetime.strptime(a, '%d-%m-%Y')
print(now-age)