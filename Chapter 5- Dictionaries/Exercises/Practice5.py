# Q5. Write a Python program to merge two dictionaries into one.
# Create a dictionary to store information
my_self1 = {
    'name' : 'Aisha',
    'Age' : '18',
    'Occupation' : 'Cyber-security analyst',
           }
    
my_self2 = {
    'Hobbies' : ['Reading', 'Going for a Run', 'Playing basketball', 'Coding'],
    'Location' : 'United Arab Emirates'
           }

# Merge 'my_self2' into 'my_self1'
my_self1.update(my_self2)

# 'my_self1' dictionary now contains all the key-value pairs of 'my_self2'
for key, value in my_self1.items():
    print(key + ":" , value)
          