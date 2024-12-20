print("Welcome to roller coaster Amusment park")
height=int(input("Enter your Height"))
bill=0
if height >= 120:
    print("You can ride the rollercoaster ")
    age =int (input("Enter your age "))
    if age <=12:
       bill=5
       print("Kids ticket is 5$")
    elif age <= 18:
           bill=7
           print("Teanagers ticket is 7$")     
    elif age >= 45 & age <=55:
        print("your ticket is free")
    else:
        bill=12
        print("Adults ticket is 12$")

    photo=input("Do you want the photo taken? Type Y for yes and N for no. ")
    if photo == "y":
        bill+=3
    print(f"your total bill is {bill} ")
else :
    print("Sorry !you have to grow taller")



   
