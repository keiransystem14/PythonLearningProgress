# Asking the customer for the price of item 1. Onced entered, the value replaced the input function.

item_1 = input("What is the price of item 1 \n")
item_2 = input("What is the price of item 2 \n")

# Calculate the total price of both items

total_before_vat = float(item_1) + float(item_2)

print(f"The total price before VAT is {total_before_vat}.")

# Example would be 5% Tax
#VAT = float(0.5)
