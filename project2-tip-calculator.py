"""
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
Write your code below this line 👇
"""

# Create a greeting for the program 
print("Welcome to the tip calculator! 💴")

# Ask the user for the bill total 
initial_bill = float(input("What was the total bill? $"))

# Ask the user for the tip percentage
tip_amount = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask the user for the number of persons
person = int(input("How many people to split the bill? "))

# Calculate the tip percentage 
tip_percent = tip_amount / 100
# Calculate the total tip amount 
total_tip = initial_bill * tip_percent
# Calculate the total bill to be paid 
total_bill = initial_bill + total_tip
# Calculate how much each person has to pay
bill_per_person = total_bill / person
# Calculate final amount rounded to 2 decimal places 
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

# Display the final total inclusive of the tip
print(f"Each person should pay: ${final_amount}")