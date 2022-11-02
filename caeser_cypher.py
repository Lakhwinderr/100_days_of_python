alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



encoded_string = ''

def shift_letter(letter, shift):
    letter_id = ord(letter) - ord('a')
    c = alphabet[(letter_id + shift) % 26]
    return c;

    
for letter in text:
    if letter != ' ':
        c = shift_letter(letter, shift)
        encoded_string+=c;
    else:
        encoded_string+=letter
print(encoded_string)