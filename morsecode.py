"""
In this program we are gonna make a program that can convert the word in to morse code and wise versa
Step1: is that you need the code that is use for the alphabets every letter have different code in dash and dots like .__.like wise
"""
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def encrypt(message):
    cipher = ''
    for letter in message.upper():
        if letter != ' ':
            try:
                cipher += MORSE_CODE_DICT[letter] + ' '
            except KeyError:
                return f"Error: Character '{letter}' is not supported in Morse code."
        else:
            cipher += ' '
    return cipher.strip()

def decrypt(morse_message):
    reverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    morse_message = morse_message.strip()
    words = morse_message.split(' / ')
    decrypted = ''
    
    for word in words:
        codes = word.split()
        for code in codes:
            try:
                decrypted += reverse_dict[code]
            except KeyError:
                return f"Error: Invalid Morse code '{code}'."
        decrypted += ' '
    return decrypted.strip()

def main():
    while True:
        user_input = input("What do you want to do? Encrypt or decrypt? (e/d) or 'q' to quit: ").lower()
        if user_input == 'e':
            message = input("Enter your message to encrypt: ")
            result = encrypt(message)
            print(f"Encrypted: {result}")
        elif user_input == 'd':
            message = input("Enter your Morse code message (use spaces between codes and '/' for word separation): ")
            result = decrypt(message)
            print(f"Decrypted: {result}")
        elif user_input == 'q':
            print("Exiting program.")
            break
        else:
            print("Please enter a valid option (e/d) or 'q' to quit.")

if __name__ == "__main__":
    main()