#Task 6:
#Write a Python program that accepts a date in the format "dd-mm-yyyy" and checks if it is a leap year. Display an appropriate message indicating whether it is a leap year or not.
import datetime
d=input()
if int(d[6:10])%4==0:
    print(True)
else:
    print(False)