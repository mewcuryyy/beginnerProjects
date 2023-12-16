import cipher_art

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar_cipher(start_text,shift_amount,shift_direction):
    end_text = ""
    if shift_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_amount
            end_text += alphabets[new_position]
        else:
            end_text += char
    print(f"Here's the {shift_direction}d result: {end_text}")

print(cipher_art.logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar_cipher(text,shift,direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
    