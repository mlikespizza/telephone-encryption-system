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


reverse_keypad = {
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z']
}

def decrypt_message(code):
    decrypted_message = ""
    for number in code: 
        if number in reverse_keypad:
            decrypted_message += reverse_keypad[number][0]
        else:
            print(f"Error: the number '{number}' is not on the keypad.")
    return decrypted_message     


while True:
    choice = input("1. Encrypt\n2. Decrypt\n3. Exit\nChoose an option: ")
    if choice == '1':
        user_text = input("Enter a message: ")
        encrypted_result = encrypt_message(user_text)
        print("Encrypted message:", encrypted_result)
    elif choice == '2':
        user_code = input("Enter a code: ")
        decrypted_result = decrypt_message(user_code)
        print("Decrypted message:", decrypted_result)    
    elif choice == '3':
        break 




