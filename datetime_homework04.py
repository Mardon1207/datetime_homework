#Task 4:
#Write a Python program that calculates the age of a person based on their birth year. Prompt the user to enter their birth year, and display their current age.
import datetime
m=datetime.date.today()
x=int(input())
n=m.year-x
print(n)