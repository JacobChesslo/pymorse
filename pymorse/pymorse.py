ALPHA_TO_MORSE = {
    # Letters
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    # Numbers
    '1': '.----', '2': '..---',  '3': '...--', '4': '....-', '5': '.....',
    '6': '-....',  '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    # Punctuations
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.', ' ': '  ',
    # TODO Add Non-Latin
    # TODO Add Prosigns
}

MORSE_TO_ALPHA = {value: key for key, value in ALPHA_TO_MORSE.items()}
# TODO Add other standards


def to_morse(message: str):
    return ' '.join([
        ALPHA_TO_MORSE[character] for character in str(message).upper() if character in ALPHA_TO_MORSE.keys()
    ])


def to_english(message: str, title: bool = False):
    message = str(message).replace('    ', '~').replace('   ', '~').replace('  ', '~')
    words = message.split('~')
    words = [word.split(' ') for word in words]
    new_words = ' '.join([
        ''.join([
            MORSE_TO_ALPHA[character] for character in word if character in MORSE_TO_ALPHA.keys()
        ]) for word in words
    ])

    if title:
        return new_words.title()
    return new_words
