#Print the title.

print("\nWelcome to the Shopping Bill Calculator!")

# Asking the shop  for the price of item 1. Onced entered, the value replaced the input function.

item_1 = input("\nWhat is the price of item 1? \n")
item_2 = input("\nWhat is the price of item 2? \n")

# Calculate the total price of both items

total_cost_before_vat = float(item_1) + float(item_2)

# VAT rate is 20% 

vat_rate = 0.2

# Calculate total price after tax

total_cost_after_vat = total_cost_before_vat * (1 + vat_rate)

# Ask user how many people to split the total

number_of_people = input("\nHow many people are contributing towards the total price? \n")

# Using division operator to calculate how much each person is contributing towards the total cost

total_amount_share = total_cost_after_vat / int(number_of_people)

# Print the total cost overall. 

print(f"\nThe total cost after VAT is £{round(total_cost_after_vat,2)}.")

#Prints the amount each person contributes towards the total cost. 

print(f"\nEach person contributes: £{round(total_amount_share,2)}\n")




