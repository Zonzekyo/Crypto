# Transposition Cipher Encrypt/Decrypt File
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import os,sys

def main():
    inputted = input('input file name(.txt file): ')
    inputFilename = str(inputted)+ '.txt'
    # BE CAREFUL! If a file with the outputFilename name already exists,
    # this program will overwrite that file.
    
    myKey = 10
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    myMode = input('encrypt or decrypt: ') # set to 'encrypt' or 'decrypt'
    outputFilename = str(inputted)+'.' +str(myMode)+'ed.txt'
    # If the input file does not exist, then the program terminates early:
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit:
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file:
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))


    if myMode == 'encrypt':
        translated = encryptMessage(myKey, content,symbols)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, content,symbols)

    # Write out the translated message to the output file:
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))

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

def decryptMessage(key,cipher,SYMBOLS):
    translated = ''
    for symbol in cipher: 
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = (symbolIndex - key)%66
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    return translated
# If transpositionCipherFile.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()