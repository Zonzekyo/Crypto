# Affine Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def main():
    # You might want to copy & paste this text from the source code at
    # https://www.nostarch.com/crackingcodes/affineHacker.py
    myMessage = """"5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        # The plaintext is displayed on the screen. For the convenience of
        # the user, we copy the text of the code to the clipboard.
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackAffine(message):
# ketikkan code dari slide 8 - 11 atau menggunakan versi Anda.
    print("Use Ctrl+C/Ctrl+D to exit")
    print("Trying keys....")
    for key in range(len(affineCipher.SYMBOLS)**2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            print("key %s is not valid for this cipher"%(key))
            continue
        decrypted = affineCipher.decryptMessage(key,message)
        if not SILENT_MODE:
            print ("Key yang dipakai %s (%s)" % (key, decrypted[:40]))
        if detectEnglish.isEnglish(decrypted):
            print()
            print("Used Key :" + str(key))
            print ("Message : %s"%(decrypted[:200]))
            print("Enter anything to continue, D to stop")
            User = input("> ")
            if User.strip().upper().startswith("D"):
                return decrypted
    return None


# If affineHacker.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()