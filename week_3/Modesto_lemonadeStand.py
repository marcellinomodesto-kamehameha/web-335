""" 
    Author: Marcellino Modesto
    Date: 6/21/2026
    File Name: Modesto_lemonadeStand.py
    Description: This file is used to create a program that simulates a lemonade stand 
"""
#Create Calculate_cost function
def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost+sugar_cost
    return total_cost
#Create calculate_profit function
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    total_cost = calculate_cost(lemons_cost, sugar_cost)
    profit = selling_price - total_cost
    return profit

# Variables to be tested
lemons_cost = 5
sugar_cost = 3
selling_price = 10

total_cost = calculate_cost(lemons_cost, sugar_cost)

# String showing the cost calculation
cost_output = str(lemons_cost) + " + " + str(sugar_cost) + " = " + str(total_cost)

# Print the cost results
print("Lemonade Cost Calculation:")
print(cost_output)


# Call calculate_profit function and store the result
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

# String showing the profit calculation
profit_output = "Selling Price (" + str(selling_price) + ") - Total Cost (" + str(total_cost) + ") = " + str(profit)

# Print the profit results
print("\nLemonade Profit Calculation:")
print(profit_output)
    
