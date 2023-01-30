# Submitted by Bhavya Patteeswaran
#  Program to build the financial calculators: an investment calculator and a home loan repayment calculator

# To use functions in math module, import math.
import math

print("Welcome to the program of financial calculators")
calculate_on = input("Choose either 'investment' or 'bond' from the menu below to proceed: \n ").lower()
print("Investment -  to calculate the amount of interest you\'ll earn on your investment")
print("Bond - to calculate the amount you\'ll have to pay on a home loan")

# if/elif/else statement 
if calculate_on == 'investment':
# Investment calculator
    P = int(input("Amount of money that user deposits: "))
    r = float(input("Number of interest rate(%): "))
    t = int(input("Number of years that money is being invested: "))
    r = round((r/100),2)
    interest = input("Choose the type of interest as 'simple' or 'compound' interest: \n").lower()
    if interest == 'simple':
         A =P*(1+r*t)
         print(f"Total amount over the simple interest: {A}.")
    elif interest == 'compound': 
         r = r/12
         t = 12*t  
         A = P* math.pow((1+r),t)
         A = round(A,2)
         print(f"Total amount over the compound interest: {A}.")
    else:
        print("Please type the right interest to calculate.")
# Home loan repayment calculator
elif calculate_on == 'bond':
    P_bond = int(input("Present value of the house: "))
    i = float(input("Number of interest rate(%): "))
    i = i / 100
    i = i / 12
    n = int(input("Number of months over which the bond will be repaid: "))
    x = (i * P_bond) / (1-(1+i) ** (-n))
    x = round(x,2)
    print(f"Repayment per month: {x}.")
else:
    print("Please type the valid input.")

