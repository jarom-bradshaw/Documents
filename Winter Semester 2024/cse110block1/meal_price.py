# What is the price of a child's meal? 4.50
# What is the price of an adult's meal? 9.00
# How many children are there? 4
# How many adults are there? 2
# What is the sales tax rate? 6

# Subtotal: $36.00
# Sales Tax: $2.16
# Total: $38.16

# drinks, appetizeers, tip percentage, here is a candy on the house


# What is the payment amount? 40
# Change: $1.84
print('Welcome to the meal price caluculator \n We help you choose healthy meals at restaurants you can afford. \n')
price_of_child_meal = float(input("What is the price of a child's meal? ")) # quotes to not mess with apostrophe mark
price_of_adult_meal = float(input("What is the price of an adult's meal? "))
number_of_children = float(input('How many children are there? '))
number_of_adults = float(input('How many adults are there? '))
sales_tax_rate = float(input('What is the sales tax rate? '))
# tip = input('Will you pay a 20% tip?')
# if tip == Yes
#     return 
tip = float(input('How much % in tips will you pay? '))

subtotal = ((price_of_child_meal*number_of_children)+(price_of_adult_meal*number_of_adults))
sales_tax_value = ((subtotal*((sales_tax_rate/100))))
tip_value = (subtotal*((tip/100)))

print()
print(f'Subtotal: ${subtotal}')
print(f'Sales Tax: ${sales_tax_value}')
print(f'Tip: ${tip_value}')
print(f'Total: ${subtotal + sales_tax_value + tip_value}')

print('Enjoy your meal or feel free to calculate the price of another meal!')