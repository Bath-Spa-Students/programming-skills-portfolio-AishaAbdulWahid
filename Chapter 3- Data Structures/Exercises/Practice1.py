'''Q1. Given a Python list, write a program to remove all occurrences of item 20.
Given list: list1 = [5, 20, 15, 20, 25, 50, 20]'''

list1 = [5, 20, 15, 20, 25, 50, 20]   # This line initializes a list named list1.

# Using list comprehension to remove item 20. (LIST COMPREHENSION: concise way of creating lists based on an existing lists.) 
#This line of code is creating a new list that includes all the elements from list1 that are not 20.
list1 = [i for i in list1 if i != 20]   # this operator '!=' is a comparison operator that checks if two values are not equal.

print(list1)