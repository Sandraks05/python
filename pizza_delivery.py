print("welcome to python pizza deliveries")
size=input("What size pizza do you want ? S,M, or L:")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
extra_cheese = input("Do you want extra chesse ? Y or N:")
bill=0
if size =="s":
    bill+=15
elif size=="m":
    bill+=20
else:
    bill+=25

if pepperoni=="y":
    if size=="s":
        bill+=2
    else:
        bill+=3

if extra_cheese =="y":
    bill+=1

print(f"total bill is ${bill}.")
   


