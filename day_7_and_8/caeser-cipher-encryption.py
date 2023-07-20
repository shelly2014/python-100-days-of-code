from art import logo 
print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caeser(text, shift, direction):
    newText = ""
    for c in text:
        if c in alphabet:
            index = alphabet.index(c)
            if direction == "encode":
                newIndex = (index + shift) % 26
            elif direction == "decode":
                newIndex = (index - shift) % 26
            newText += alphabet[newIndex]
        else:
            newText += c
    print(f"The {direction}d text is:\n{newText}")

choice = "yes"
while(choice == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text=text, shift=shift, direction=direction)
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()

