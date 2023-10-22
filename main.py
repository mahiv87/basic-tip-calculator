# Welcome message
print("Welcome to the tip calculator")

# Total cost of the bill
bill_total = input("What was the total bill?")

# Choose a percentage
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15?")

# Input that asks user how the bill will be divided
bill_split = input("How many people will split the bill?")

# Converting the bill total from string to float
bill_to_int = float(bill_total)

# Converting percentage from string to int
tp_to_int = int(tip_percentage)

# Convert percentage to decimal
percentage = tp_to_int / 100

# Convert divider from string to int
split_to_int = int(bill_split)

# Calculate the tip
tip = bill_to_int * percentage

# Calculate total bill
total_bill = bill_to_int + tip

# Calculate how much each person should pay
bill_per_person = total_bill / split_to_int

# Round the bill per person to two decimal places
final_amount = round(bill_per_person, 2)
# Formats the final_amount to use .00
final_amount = "{:.2f}".format(bill_per_person)

# Convert the tip to currency format using F-String
currency_converter = f"${final_amount}"

# Print the results
print(f"Each person should pay: {currency_converter}")