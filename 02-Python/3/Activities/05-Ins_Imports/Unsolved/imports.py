# Import my functions from functions.py
import functions
functions.print_goodbye()

#call the print_hello directly
from functions import print_hello
print_hello()


#Import numpy library
import numpy

# import numpy financial
import numpy_financial as npf


##initialize variables
interest_rate = 0.1
cash_flows = [-1000, 400, 400, 400, 400]


#calculate NPV, we are going to call a function from numpy financial, which is npv
net_present_value = npf.npv(interest_rate, cash_flows)
print(f"NPV = {net_present_value}")
