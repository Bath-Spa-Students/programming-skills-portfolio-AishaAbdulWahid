'''Q4. Assume the lists numbers1 has 100 elements and numbers2 is an empty list. Write code that 
       copies the values in numbers1 to numbers2.'''

# there are 300 elements in 'numbers1'
numbers1 = list(range(1, 101))

# 'numbers2' is an empty list 
numbers2 = []

# Using a for loop to copy elements from 'number1' to 'numbers2'
for number in numbers1:   # This line creates a for loop that iterates each element the 'numbers1' list.
    numbers2.append(number)   # It adds the current 'numbers' to the end of 'numbers2' list using append() funtion.

# 'numbers2' now contains the elemenst of 'numbers1'
print(numbers2)   # This line is outside the for loop. It print the 'numbers2' list.