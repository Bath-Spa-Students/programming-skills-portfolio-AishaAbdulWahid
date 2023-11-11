# Q4. Write a Python program that uses the break statement to exit a for loop when a specific condition is met.

# Use a for lopp to iterate over the numbers from 1 to 10
for number in range(1, 11):
    # Print the current number
    print(number)

    # If the current number is 5, break the loop
    if number == 5:
        print("NUmber 5 is found breaking the loop.")
        break 
    