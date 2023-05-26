#Task 5:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and determines the day of the week on which that date falls.
import datetime
d=input()
if int(d[6:10])%4==0:
    print(True)
else:
    print(False)