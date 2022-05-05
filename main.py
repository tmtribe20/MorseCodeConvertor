# This is a simple program to convert text to morse code.

# Dictionary containing the morse code.
MORSE_CODE = {'0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', 'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..'
              }

# Reverse the key values in the dictionary to get the morse code.
REVERSE_CODE = {value: key for key, value in MORSE_CODE.items()}


# Main program.
def main():
    while True:
        print("Do you want to encode 1 , decode 2 or exit 3 ?")
        choice = input()
        if choice == '1':
            print("Enter your message:")
            message = input()
            print(convert_to_morse(message))
        elif choice == '2':
            print("Enter your morse code message to decode")
            morse_code = input()
            print(decode_morse(morse_code))
        elif choice == '3':  # Exit the program.
            print("Exiting...")
            break
        else:
            print("Invalid selection. Try again.")

# Function to convert text to morse code.
def convert_to_morse(message):
    message = message.upper()  # Convert to uppercase.
    morse_code = ''
    for letter in message:
        if letter in MORSE_CODE:  # Check if the letter is in the dictionary.
            morse_code += MORSE_CODE[letter] + ' '
        else:
            morse_code += ' '
    return morse_code


def decode_morse(morse_code):
    morse_code = morse_code.split(' ')  #
    message = ''  # setup empty  for decoded message.
    for code in morse_code:
        if code in REVERSE_CODE:
            message += REVERSE_CODE[code]
        else:
            message += ' '  # Add a space if the code is not found
    return message


if __name__ == '__main__':  # Run the main program.
    main()
