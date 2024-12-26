# Define a function to calculate total price including tax
def calculate_total_with_tax(prices, tax_rate):
    """
    Calculate the total price including tax.
    
    Parameters:
    prices (list of float): List of item prices.
    tax_rate (float): Tax rate as a decimal (e.g., 0.07 for 7% tax).
    
    Returns:
    float: Total price including tax.
    """
    total = sum(prices)
    total_with_tax = total * (1 + tax_rate)
    return total_with_tax

# List of item prices
item_prices = [19.99, 5.49, 3.50, 12.99]

# Tax rate (e.g., 7% tax)
tax_rate = 0.07

# Calculate the total price including tax
total_price = calculate_total_with_tax(item_prices, tax_rate)

print("Total Price with Tax: $", total_price)