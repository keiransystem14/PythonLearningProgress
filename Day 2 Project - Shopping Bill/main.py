# Asking the shop  for the price of item 1. Onced entered, the value replaced the input function.

item_1 = input("What is the price of item 1? \n")
print("\n")
item_2 = input("What is the price of item 2? \n")
print("\n")
# Calculate the total price of both items

total_before_vat = float(item_1) + float(item_2)

# VAT rate is 20% 

vat_rate = 0.2

# Calculate total price after tax

total_after_vat = total_before_vat * (1 + vat_rate)

# Ask user how many people to split the total

num_of_people = input("How many people are contributing towards the total price? \n")
print("\n")
# Using division operator to calculate how much each person is contributing towards the total price
total_share = total_after_vat / int(num_of_people)

# Print the total price overall. 
print(f"The total price after VAT is £{round(total_after_vat,2)}.")
print("\n")

#Prints the amount each person contributes towards the total price. 
print(f"Each person contributes: £{round(total_share,2)}")




