'''Use a dictionary to store information about a person you know.Store their first name,\
   last name, age, and the city in which they live. You should have keys such as first_name,\
   last_name, age, and city. Print each piece of information stored in your dictionary.'''

# Define a dictionary to store the information 
individual = {
    "first_name": "James",
    "last_name": "Charles",
    "age": "28",
    "HomeTown": "New York"
             }

# Print each piece of information stored in the dictionary
for key, value in individual.items():
    print(f"{key}: {value}")
