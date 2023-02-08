# Python script to check the system information
import os
import datetime as dt
import pyfiglet as pyg

banner = pyg.figlet_format("SYS INFO")
print(banner)

print('\t \tMade by KANE') 
print("""""")
print("This script provides you following options :")
options = ['CPU Count' ,'Date-time information']
count = 1
for i in options:
    print(count , ")" , i)
    count = count + 1


user_input = input("Enter option : ")

if (user_input == "1"):
    print("CPU COUNT : " , os.cpu_count())
elif (user_input == "2"):
    print("Date and time is : " ,dt.datetime.today())
else:
    print("Not a valid input")

