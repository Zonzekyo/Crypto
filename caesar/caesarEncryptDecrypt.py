def main():
    message = 'This is my secret message.'

    key = 13
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    cipher = encryptCaesar(message,key)
    print (cipher)
    plain = decryptCaesar(cipher,key)
    print(plain)
def encryptCaesar(message,key):
    translated = ''
    for symbol in message: 
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = (symbolIndex + key)%66
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    return translated

def decryptCaesar(cipher,key):
    translated = ''
    for symbol in cipher: 
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = (symbolIndex - key)%66
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    return translated

if __name__ == "__main__":
    main()