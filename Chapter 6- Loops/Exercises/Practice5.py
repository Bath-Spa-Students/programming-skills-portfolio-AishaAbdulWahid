'''Q5. Write a Python program that uses a while loop to find the largest number among a series of user-input values\
      until they enter '0' to exit the loop.'''

# Print a message asking the user to enter a numbers greater than '0'
print("Enter a numbers greater than '0'.")

# Print a message telling the user to enter '0' to finish
print("Enter '0' to finish.")

# Initialize maximum as the lowest possible integer value
max_num = float('-inf')

# Start a whiel loop that runs until 0 is entered 
while True:
    # Prompt the user to enter a number and convert it to a float 
    num = float(input("Please enter a number: "))

    # If the user enters '0', break the loop 
    if num == 0:
        break
    #If the entered number is greater than the curent maximum, update the maximum
    elif num > max_num:
        max_num = num

# After the loop ends, print the maximum number 
print("The largest number is", max_num)
