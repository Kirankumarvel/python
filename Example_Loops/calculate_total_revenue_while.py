# List of customer orders
orders = [
    {"order_id": 1, "amount": 99.99},
    {"order_id": 2, "amount": 49.50},
    {"order_id": 3, "amount": 25.75},
    {"order_id": 4, "amount": 150.00},
    {"order_id": 5, "amount": 75.25}
]

# Calculate total revenue until a specific order ID is encountered
total_revenue = 0.0
index = 0
while index < len(orders) and orders[index]["order_id"] != 4:
    total_revenue += orders[index]["amount"]
    index += 1

print("Total Revenue until Order ID 4: $", total_revenue)