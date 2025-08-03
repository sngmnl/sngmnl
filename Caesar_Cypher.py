from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    decypher_text = ""
    for letter in original_text:
        if letter in alphabet:
            unshifted_position = alphabet.index(letter) - shift_amount
            unshifted_position %= len(alphabet)
            decypher_text += alphabet[unshifted_position]
        else:
            decypher_text += letter
    print(f"Here is the encoded result: {decypher_text}")

def ceaser(original_text, shift_amount, direction_input):
    if direction_input == "encode":
        encrypt(original_text, shift_amount)
    elif direction_input == "decode":
        decrypt(original_text, shift_amount)

ceaser(original_text=text, shift_amount=shift, direction_input=direction)
repeat = True
while repeat:

    guess2 = input(f"Type 'yes' if you'd like to go again, otherwise type 'no': ").lower()

    if guess2 == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaser(original_text=text, shift_amount=shift, direction_input=direction)
    else:
        repeat = False






