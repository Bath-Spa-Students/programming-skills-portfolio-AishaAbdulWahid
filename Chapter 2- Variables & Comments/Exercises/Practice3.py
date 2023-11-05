'''Write a python program that takes an input from user and then type cast those values to string,/
   int and float in the separate variables. Print all the variables.'''

# Take an input from the user 
input_value = input("Enter a number: ")   # This line asks the user to input a number.

# Type cast the input to string, int, and float
string_value = str(input_value)   # The str() function is used to convert the user input into a string.
int_value = int(input_value)   # The int() function is used to convert the user input into an integer.
float_value = float(input_value)   # The float() function is used to convert the user input into a float.

# Print all the variables
print(f"String value:", {string_value})
print(f"Integer value:", {int_value})
print(f"Float value:", {float_value})
