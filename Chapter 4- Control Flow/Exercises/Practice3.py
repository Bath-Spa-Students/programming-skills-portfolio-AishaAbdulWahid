'''Q3. Write a python program with nested decision structures that perform the following: 
       If amount1 is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2.'''

# Assuming 'amount1' and 'amount2' are your variable 
amount1 = 15 
amount2 = 50

# Using an if statement to check the conditions
if amount1 > 10 and amount2 < 100:
    # If both conditions are met, find the greater of 'amount1' and 'amount2'
    if amount1 > amount2:
        print("The greater amount is:", amount1)
    else:
        print("The greater amount is:", amount2)
