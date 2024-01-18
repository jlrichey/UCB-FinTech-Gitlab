driverless_car = True

if driverless_car == True:
    # Do something 
    print("Oh no !! the driver is asleep!!! What do we do?")
    print()
    print("All good, auto pilot started")
else:
    #Do something else
    print("Oh noo the driver is asleep Mayday MAYDAY!!!!")

    
is_raining = False
if is_raining:
    print("Bring an umbrella!")
else:
    print("Leave the umbrella at home!")

    
    
pedestrian = True
if not pedestrian:
    immediate_action = "drive"
else:
    immediate_action = "stop"
    

x = 5
if x == 1:
    print("x is equal to 1")
    
# Demostrate using varaibles to store conditions
x = 5
y = 10
if x == 5 and y <= 10:
    print("Both values returned True")
    
# how to check inequality
y = 9
if y != 1:
    print("y is not equal to 1")
    

# Nested if statements with insurance premium predictor
accident = True
at_fault = False
accident_forgiveness = True
elite_status = True

increase_insurance_premium = True

print("Insurance premium will increase. True or False?")

# Nested Conditional Statements
if accident:
    if at_fault and accident_forgiveness:
        increase_insurance_premium = False
    elif at_fault and not accident_forgiveness and not elite_status:
        increase_insurance_premium = True
    else:
        increase_insurance_premium = False
elif not accident and elite_status:
    increase_insurance_premium = False
else:
    increase_insurance_premium = True

print(f"Prediction: {increase_insurance_premium}")