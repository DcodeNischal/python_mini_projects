# Inputs for the program:
amount = float(input("Enter the amount of the bill : ").strip('$'))
tip = int(input("Enter the tip percentage : ").strip('%'))
tax = int(input("Enter the tax percentage : ").strip('%'))

# Calculate the tip and tax
tax_amount = amount * tax/100
tip_amount = amount * tip/100
# Calculate the total amount
total = amount + tax_amount + tip_amount
# Print the tip, tax and total amount
print("The tip amount is : $ ", tip_amount)
print("The tax amount is : $ ", tax_amount)
print("The total amount including tax and tip is : $ ", total)
