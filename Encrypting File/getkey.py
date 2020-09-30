
    noteFile = open('note.txt')
    lines = noteFile.readlines()
    key = lines[0]
    symbols = lines[1]
    noteFile.close()
    print(key)
    print(symbols)