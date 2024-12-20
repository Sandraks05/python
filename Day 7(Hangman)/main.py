import random
from hangman_words import words_list
from hangman_art import stages,logo

print("\t\t LETS PLAY WORD GAME ")
print(logo)
#choosing random word 
chosen_word = random.choice(words_list)

lives=6
#place holder created
length= len(chosen_word)
placeholder=""
for position in range(0,length):
   placeholder +="_"
print(placeholder)

#guess letter
game_over = False
correct_letters = []

while not game_over:
    print(f"************{lives}/6 lives left*************")
    guess=input("guess a letter\t").lower()
    print("Guessed letter is : ",guess)
    if guess in correct_letters:
          print(f"You already guessed{guess}")
    display=""
    for letter in chosen_word:
        if letter == guess:
                display+= letter
                correct_letters.append(guess)
        elif letter in correct_letters:
                display+=letter
        else:
                display+="_"
                
    print(display)
    if guess not in chosen_word:
          print("That's not the letter you lose a life ")
          lives-=1
          if lives ==0:
                print(f"you lose.\n The word is {chosen_word}")

    if "_" not in display :
            game_over=True
            print("you win")
    print(stages[lives])

