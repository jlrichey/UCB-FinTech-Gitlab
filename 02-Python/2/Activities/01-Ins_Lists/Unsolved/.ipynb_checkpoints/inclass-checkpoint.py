"""
  Pseudocode for a cheer-leading program:

  1. Initialize "cheer" variable to a string to be cheered
  2. Create a for loop and iterate through each character in "cheer" variable
      2.1 Print each letter to screen with a cheer
  3. Print exclamations to screen ("Woohoo!!!")
"""

# # create a variable 
# cheer_list = ["UCBFintech, LA_Galaxy, Dodgers, Lakers"]


# #loop through the list
# #Identify the length of the list and loop thru the length
# for item in range(len(cheer_list)):
    
#     for letter in cheer_list[item]:
#         #print me each letter with cheer variable
#         print("Give me a " + letter + "!")
#         print(letter + "!")
    
# #print exclamation to screen ("Woohoo!!!")

# print("\nWhat does that spell!!")
# print(cheer_list[item] + "\nWoohoo!!!" + " " + cheer_list[item] + "!")


# Index: 0 = "green", 1 = "blue", 2 = "red", 3 = "purple"
color_hats = ["green", "blue", "red", "purple"]

#different data types

my_favorite_things = ["Chocolate", 9, ["beach", "mountains"], 10.5, "breakfast_tacos"]


# Create a list of Pokemon
print("Creating a list of Pokemon...")
pokemon = ["Pikachu", "Charizard", "Bulbasaur", "Gyarados", "Dragonite", "Onyx"]
print(pokemon[2])
print()

# PRint the elements from index 2 and index 5
# print(pokemon[2:5]) # list[start:end]

#Slice my list from start index to the end

print(pokemon[3:])

#print the first 3 elements of the list

print(pokemon[:3])

#print ever other element
print(pokemon[::2])

#print the last element of the list
print(pokemon[-1])

#change the name of a element ina list

# print("changing names of the first element")
# pokemon[0] = "FinTech"

# print(pokemon)
# print()


#Add fintech to the list
print("Add element to the list by using append")
pokemon.append("Fintech")
print(pokemon)
print()

# see how many elements the list has

print("the number of elements")
print(len(pokemon))


#Identify the index of a element in a list in this case Bulbasaur

print("identify the index of Bulbasaur")
print(pokemon.index("Bulbasaur"))
print()

#remove the index 2 by name

print("remove index 2")
pokemon.remove("Bulbasaur")
print(pokemon)
print()

#remove by index without knowing the name of the list you will use pop()
print("remove index 3")
pokemon.pop(3)
print(pokemon)
print()