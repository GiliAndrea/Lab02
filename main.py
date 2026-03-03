import translator as tr

t = tr.Translator()

while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print()
        txtIn = input()
        pass

    if int(txtIn) == 2:
        query = input("Ok, quale parola devo cercare?\n\n")
        print(f"{query}")
        print(f"{t.handleTranslate(query)}")

    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        break