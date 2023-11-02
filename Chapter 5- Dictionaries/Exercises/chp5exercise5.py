# empty list to store the pets in.
pets = []

# individual pets,
#  store each one in the list.
pet = {
    "animal type": 'lamb',
    "name": 'lopi',
    "owner": 'pheobe',
    'weight': 600,
    'eats': 'vitamins, vegetables, fruits',
}
pets.append(pet)

pet = {
    'animal type': 'raccon',
    'name': 'stiffie',
    'owner': 'rinoa',
    'weight': 9,
    'eats': 'everything, anything',
}
pets.append(pet)

pet = {
    'animal type': 'calf',
    'name': 'pepero',
    'owner': 'kairi',
    'weight': 90,
    'eats': 'seeds, vitamins, vegetables, fruits',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
        