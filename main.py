import translator

t = translator.Translator()

svolgimento = True
while(svolgimento):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        ricerca = input("Ok, quale parola devo aggiungere?\n\n")
        ricerca = ricerca.lower()
        elementi = ricerca.split(" ", 1)
        risultato = (elementi[0], elementi[1])
        print(list(risultato))
        t.handleAdd(risultato)

    if int(txtIn) == 2:
        query = input("Ok, quale parola devo cercare?\n\n")
        print(f"{query}")
        query = query.lower()
        print(f"{t.handleTranslate(query)}")

    if int(txtIn) == 3:
        query = input("Ok, quale parola devo cercare?\n\n")
        print(f"{query}")
        query = query.lower()
        print(f"{t.handleWildCard(query)}")

    if int(txtIn) == 4:
        t.dizio.stampaTot()

    if int(txtIn) == 5:
        svolgimento = False