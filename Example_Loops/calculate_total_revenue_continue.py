# List of customer orders
orders = [
    {"order_id": 1, "amount": 99.99},
    {"order_id": 2, "amount": 49.50},
    {"order_id": 3, "amount": 25.75},
    {"order_id": 4, "amount": 150.00},
    {"order_id": 5, "amount": 75.25}
]

# Calculate total revenue, skipping orders below $50
total_revenue = 0.0
for order in orders:
    if order["amount"] < 50:
        continue
    total_revenue += order["amount"]

print("Total Revenue excluding orders below $50: $", total_revenue)