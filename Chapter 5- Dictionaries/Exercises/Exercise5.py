# Define several dictionaries for different pets
pet_1 = {"animal": "parrot", "owner": "Bill"}
pet_2 = {"animal": "horse", "owner": "Ahmad"}
pet_3 = {"animal": "rabbit", "owner": "Emily"}

# Store these dictionaries in a list
pets = [pet_1, pet_2, pet_3]

# Loop through the list and print the information about each pet
for pet in pets:
    print(f"{pet['owner']} is the owner of a {pet['animal']}.")
    