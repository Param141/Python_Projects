
import art

print(art.logo)






alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#position in the alphabet array from 0 index to 25 index



# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) # doing modulo 26 to keep in the fixed range as 9 added to z index 25 will give 34 and alphabet[34] is index out of bound
#         cipher_text += alphabet[shifted_position] # the text we found after shifting the values
#     print(f"Here is the encoded result: {cipher_text}")


# encrypt(original_text=text, shift_amount=shift)
# #can directly pass the parameters from function no need to take seperately


# def decrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {cipher_text}")


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode": # brought this if statement to the top so that we can use the same function for both encoding and decoding
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:  # if the letter is not in the alphabet list then we don't need to shift it or want it to get lost 
            # this is for spaces and special characters like !, @, #,1,2,3 etc.
            output_text += letter  # copy the letter as it is
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
# End of the code snippet