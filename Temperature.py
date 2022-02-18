'''
Name: Gabriel Ung
Student ID: s10036787
AT 1 Coding Assignment - ICTPRG405
This program will take temperature input in degree Celsius and checks if temperature is
freezing or above freezing
Version: 1.0
'''

# Ask user for temperature input
temp = int(input("Please enter temperature in degree Celsius: "))

# Checks temperature range and returns result
if(temp == 0):
    print("Freezing")
elif(temp > 0):
    print("Above Freezing")
else:
    print("Freezing")
