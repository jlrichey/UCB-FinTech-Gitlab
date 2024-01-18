"""
  Pseudocode for a cheer-leading program:

  1. Initialize "cheer" variable to a string to be cheered
  2. Create a for loop and iterate through each character in "cheer" variable
      2.1 Print each letter to screen with a cheer
  3. Print exclamations to screen ("Woohoo!!!")
"""

# # create a variable 
# cheer = "UCB Fintech"


# for letter in cheer:
#     #print me each letter with cheer variable
#     print("Give me a " + letter + "!")
#     print(letter + "!")
    
# Print exclamation to screen ("Woohoo!!!")

# print("\nWhat does that spell!!")
# print(cheer + "\nWoohoo!!!" + " " + cheer + "!")
    
"""
Pseudocode for calculating simple interest:

  1. Initialize "principal", "interest_rate", and "time_period" variables to a float
  2. Compute "simple_interest" by multiplying principal, interest_rate, and time_period
  3. Print(simple_interest)
"""
# # Define variables 
# principal = 300000.00
# interest_rate = 0.10
# time_period = 5.0

# #Computer simple interest rate
# simple_interest = principal * interest_rate * time_period

# # Print the results
# print(f"Simple interest rate for your purchase is: {simple_interest}")


"""
Conditionally Yours

Pseudocode:
1. Initialize variables original_price, current_price, increase, percent_increase, recommendation, threshold_to_buy, and threshold_to_sell
2. Compute increase
3. Compute percent_increase
4. IF percent_increase is greater than or equal to threshold_to_sell
        THEN Set recommendation to "sell"
    ELSE IF percent_increase is less than or equal to threshold_to_buy
        THEN set recommendation to "buy"
    ELSE IF percent_increase is less than threshold_to_sell and greater than threshold_to_buy
        THEN set recommendation to "hold"
    ELSE
        THEN print("Not enough data to make a decision. Need human input")
5. Print("Recommendation: " + recommendation)
"""

# Declare variables

original_price = 1550.00
current_price = 1650.00

# calcute increase

increase = current_price - original_price

#How do calculate percent_increase 
percent_increase = (increase / original_price)*100
recommendation = "buy"
threshold_to_buy = 1.00
threshold_to_sell = 100.00

if percent_increase >= threshold_to_sell:
    recommendation = "sell"
elif percent_increase <= threshold_to_buy:
    recommendation = "buy"
elif percent_increase < threshold_to_sell and percent_increase > threshold_to_buy:
    recommendation = "hold"
else:
    print("Not enough data to make a decision. Need human input")
    
print("Recommendation: " + recommendation)
print()

    

