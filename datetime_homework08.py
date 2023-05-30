#Task 8:
#Write a Python program that subtracts 10 hours from the current time and displays the resulting time.
import datetime
now=datetime.datetime.now()
a=datetime.timedelta(hours=10)
print(now-a)