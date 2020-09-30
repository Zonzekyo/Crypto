plaintext = 'YAMAMOTO'
encrypted = 'PRDRDFKF'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated=''
    for symbol in encrypted:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = (symbolIndex - key)%len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    if translated == plaintext:
        print ('The key is : %s' %(key))