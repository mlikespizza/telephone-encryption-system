keypad = {
    'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7',
    'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9'

}

def encrypt_message(message):     

    encrypted_message = ""

    for letter in message: 
        if letter.upper() in keypad:
            encrypted_message += keypad[letter.upper()]
        else:
            print(f"Error: the character '{letter}' is not on the keypad.")
    return encrypted_message

while True:
    choice = input("1. Encrypt\n2. Exit\nChoose an option: ")
    if choice == '1':
        user_text = input("Enter a message: ")
        encrypted_result = encrypt_message(user_text)
        print("Encrypted message:", encrypted_result)
    elif choice == '2':
        break 



#def decrypt_message(code):


