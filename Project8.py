alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caeser(encode_or_decode):
    def encrypt(text, shift_amount):
        encode_text_2 = []
        encode_list = text
        for letter in encode_list:
            if letter not in alphabet:
                encode_text_2 += letter
                continue
            if alphabet.index(letter) + shift > 25:
                shift_2 = len(alphabet)- 1 - alphabet.index(letter)
                encoded = alphabet.index("a") + shift_amount - shift_2 - 1
                encode_text = alphabet[encoded]
                encode_text_2.append(encode_text)
            else:
                encoded = alphabet.index(letter) + shift_amount
                encode_text = alphabet[encoded]
                encode_text_2.append(encode_text)
        final_text = ''.join(encode_text_2)
        print(f"Here is the encoded text: {final_text}")


    def decrypt(text, shift_amount):
        encode_text_2 = []
        encode_list = text
        for letter in encode_list:
            if letter not in alphabet:
                encode_text_2 += letter
                continue
            if alphabet.index(letter) + shift < 0:
                shift_2 = len(alphabet) + 1 + alphabet.index(letter)
                encoded = alphabet.index("z") - shift_amount + shift_2 + 1
                encode_text = alphabet[encoded]
                encode_text_2.append(encode_text)
            else:
                encoded = alphabet.index(letter) - shift_amount
                encode_text = alphabet[encoded]
                encode_text_2.append(encode_text)
        final_text = ''.join(encode_text_2)
        print(f"Here is the encoded text: {final_text}")

    if direction == "encode":
        encrypt(text, shift)
    if direction == "decode":
        decrypt(text, shift)


Game = True
while Game is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(direction)
    decision = input("Do you want to encode or decode again? Press \"Yes\" to continue or \"No\" to end\n")
    if decision == "yes" or decision == "Yes":
        continue
    else:
        Game = False