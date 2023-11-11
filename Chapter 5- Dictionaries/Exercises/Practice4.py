# Q4. Write a Python program to iterate through both the keys and values of a dictionary and print them.
# Create a dictionary to store information
my_self = {
    'name' : 'Aisha',
    'Age' : '18',
    'Occupation' : 'Cyber-security analyst',
    'Hobbies' : ['Reading', 'Going for a Run', 'Playing basketball', 'Coding'],
    'Location' : 'United Arab Emirates'
          }

# Use a for loop to print each key- value pair
for key, value in my_self.items():
    print(key + ":", value)