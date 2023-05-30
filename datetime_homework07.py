#Task 7:
#Write a Python program that adds 5 days to the current date and displays the resulting date.
import datetime
s=input()
now=datetime.datetime.strptime(s, '%d-%m-%Y')
a=datetime.timedelta(days=5)
print(now+a)