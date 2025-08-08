print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $")) # bill amount as float
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2) # rounding to 2 decimal places after division
print(f"Each person should pay: ${final_amount}")

# This code calculates the tip and splits the bill among a given number of people.
# The user is prompted to enter the total bill, tip percentage, and number of people.
#12%= 12/100 = 0.12 and 150*0.12 = 18 gives the 12% of 150 
#to add the tip in final bill we add the tip to the bill so (150 + 0.12*150)
# or can also write it as 150*1.12 by taking 150 as common factor
# so bill = bill*(1+tip/100)