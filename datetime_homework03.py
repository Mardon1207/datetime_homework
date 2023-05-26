#Task 3:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and calculates the number of days between the current date and the entered date.
import datetime
y=datetime.date.today()
d=input()
i=0
m=int(d[0:2])
i+=y.day-m
m=int(d[3:5])
if y.month>=m:
    i+=abs(y.month-m)*30
    m=int(d[6:10])
    i+=(y.year-m)*365
else:
    i+=abs(y.month+12-m)*30
    m=int(d[6:10])
    i+=(y.year-1-m)*365
print(i)