#encoding and decoding a message
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print('''
░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄
░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀''')
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
            shift_amount = -shift_amount
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the  result: {output_text}")
should_continue = True
while should_continue == True :
    direction= input("Type 'encode' to encrypt , type 'decode' to decrypt:\n".lower())
    text = input("Type your message: \n".lower())
    shift=int(input("Type the shift number: \n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart = input("Type 'Yes' if you want to continue or type 'No'. \n" .lower())
    if restart == "no":
        should_continue = False
        print("GoodBye")

