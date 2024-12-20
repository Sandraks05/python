import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '<', '>', '?']
print("Welcome to pypassword Generator!")
nr_letters=int(input(f"How many letters would you like in your password?\n"))
nr_symbols=int(input(f"How many symbols would you like\n"))
nr_numbers=int(input(f"how many numbers would you like\n"))
password=""
for char in range(0, nr_letters):
    random_letters=random.choice(letters)
    password+=random_letters
for num in range(0, nr_numbers ):
    random_number=random.choice(numbers)
    password+=random_number
for sym in range(0, nr_symbols ):
   password+=random.choice(symbols)
password_list=list(password)
random.shuffle(password_list)
shuffled_password=''.join(password_list)
print(f"your password is  {shuffled_password}")