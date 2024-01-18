"""
The final results should have the following outputs"
1. Number of days that of the total list of tips
2. Total of tips
3. Daily average
4. Least amount of tips I got (minimum)
    If my minimum is equal to 0, minimum to that amount
    otherwise, elif my amount is less than my minimum, 
    assign that minimum to my amount. 
5. Maximum amount of tips that I got
     if my amount is grater than the maximum 
     maximum make it equal to the amount

I want that output base on a cash_tips variable
"""

# list my cash_tips variable

cash_tips = [50, 100, 80, 90, 200, 120]

# start my metrics variables
count = 0
total = 0
average = 0
minimum = 0
maximum = 0

# I want to see every tip on my list
for amount in cash_tips:
#     print(amount)
    #Calculate the cumulative sum of my tips
    
    # approach 1 to calculate total or cumulative sum
#     total = total + amount
    
    # approach 2 to calculate total or cumulative sum
    total += amount
    count += 1
    # calculate the logic for minimum
    if minimum == 0:
        minimum = amount
    elif amount < minimum:
        minimum = amount
        
    #logic for maximun 
    if amount > maximum:
        maximum = amount
    
average = round(total / len(cash_tips),2)

print("---------Summary Statistics----------")
print(f"Number of Days: {count}")
print(f"Total Tips: ${total}")
print(f"Daily Average: ${average}")
print(f"Least Amount of Tips: ${minimum}")
print(f"Maximum Amount of Tips: ${maximum}")