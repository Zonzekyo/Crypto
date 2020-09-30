# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip

def main():
    myMessage = '''Augusta Ada King-Noel, Countess of Lovelace (10 December 1815 - 27 November 1852) was an English mathematician and writer, chiefly known for her work on Charles Babbage's early mechanical general-purpose computer, the Analytical Engine. Her notes on the engine include what is recognised as the first algorithm intended to be carried out by a machine. As a result, she is often regarded as the first computer programmer.'''
    myKey = 13

    ciphertext = encryptMessage(myKey, myMessage)
    

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard.
    pyperclip.copy(ciphertext)


def encryptMessage(key, message,SYMBOLS):
    # Each string in ciphertext represents a column in the grid.
    translated = ''
    for symbol in message: 
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = (symbolIndex + key)%66
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    return translated


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()