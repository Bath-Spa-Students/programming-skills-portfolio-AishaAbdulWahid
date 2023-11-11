'''Q5. Write a Python program that uses the elif statement to determine the season based on the 
       month provided as input.'''

# Get the month from the user
month = input("Enter the month: ")

# Using an if-elif statements to determine the season
if month in ['December', 'January', 'February']:
    print("The season is WINTER!")
elif month in ['March', 'April', 'May']:
    print("The season is SPRING!")
elif month in ['June', 'July', 'August']:
    print("The season is SUMMER!")
elif month in ['September', 'October', 'November']:
    print("The season is AUTUMN!")
else:
    print("Invalid month")
