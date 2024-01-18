for x in range(5):
    print(x)

    
print("------------------")

phrase = "Hello world this is my first python code"

for letters in phrase:
    print(letters)
    
print("------------------")

desire_number = 15

for number in range(20):
    if (number == desire_number):
        continue     
    print(number)
    
print("------------------")

# Initial counter

counter = 1

while counter < 15:
    print(counter)
    
    #increment of the counter is 1
    counter = counter + 1   # to commment a line (ctrl + ?)
    
    
While loop until a condition is met

run = "y"

while run == "y":
    print("Hi!!")
    run = input("To run again, Enter 'y'")
