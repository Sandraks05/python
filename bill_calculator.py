import math
print("Welcome to calculator")
bill=float(input("What was the total bill?"))
tip=int(input("How much would you like to give ... 10,12,15?"))
split_num =int(input("How many people to split the bill?"))
tip_percent = tip/100
total_bill = bill+bill*tip_percent
split_bill = total_bill/split_num
BILL= round(split_bill,2)
print(f"Bill per person is {BILL}")