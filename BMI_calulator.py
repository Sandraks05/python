weight =float(input("Enter your weight"))
height=float(input("Enter your Height"))
bmi=weight / (height**2)
if bmi <= 18.5:
    print("You are so small come after you grow up ")
elif bmi < 25:
    print("Lets enjoy the ride . you're perfect size ")
else:
    print("Go to gym not to amusement park ")


