# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5 # (1,2,3,4,5)

# The list used to store all of the candies selected inside of
candyCart = []

# Print out options
for i in range(len(candyList)):
    print("[" + str(i) + "] " + candyList[i])
    
# Run the question
print("Which cnady would you like to bring home")

for number in range(allowance):
    enter_input = input("Input the number of cnady you want: ")
    
    #Add the candy at the index chosen for th candy_list
    candyCart.append(candyList[int(enter_input)])
    
print("I brought home with me... ")

for candy in candyCart:
    print(candy)

