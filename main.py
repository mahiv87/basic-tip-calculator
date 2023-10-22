print("Welcome to the tip calculator")

bill_total = input("What was the total bill?")

tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15?")

bill_split = input("How many people will split the bill?")

bill_to_int = int(bill_total)

tp_to_int = int(tip_percentage)

percentage = tp_to_int / 100

split_to_int = int(bill_split)


