# List of item prices as strings
item_prices = ["19.99", "5.49", "3.50", "12.99"]

# Convert string prices to floats and calculate the total cost
total_cost = 0.0
for price in item_prices:
    total_cost += float(price)

print("Total Cost: $", total_cost)