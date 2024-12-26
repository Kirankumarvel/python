# This first line is provided for you

# User worked hours
hrs = input("Enter Hours: ")

# User rate per hour
rate = input("Enter Rate per Hour: ")

# Convert input strings to float numbers
hrs = float(hrs)
rate = float(rate)

# Compute gross pay
pay = hrs * rate

# Print the gross pay
print("Pay:", pay)