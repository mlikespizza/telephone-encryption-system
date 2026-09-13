keypad = {
    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999'

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
    '2': 'A', '22' : 'B', '222': 'C',
    '3': 'D', '33': 'E', '333': 'F',
    '4': 'G', '44': 'H', '444': 'I',
    '5': 'J', '55': 'K', '555': 'L',
    '6': 'M', '66': 'N', '666': 'O',
    '7': 'P', '77': 'Q', '777': 'R', '7777': 'S',
    '8': 'T', '88' : 'U', '888' : 'V',
    '9': 'W', '99': 'X', '999': 'Y', '9999': 'Z'
}

def decrypt_message(code):
    decrypted_message = ""

    i = 0
    while i < len(code):
        set_of_numbers = code[i]
        while i + 1 < len(code) and code[i + 1] == code[i]:
            set_of_numbers += code[i + 1]
            i += 1
        i += 1

        if set_of_numbers in reverse_keypad:
            decrypted_message += reverse_keypad[set_of_numbers]
        else:
            print(f"Error: the number '{set_of_numbers}' is not on the keypad.")
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




