import dictionary


class Translator:
    def __init__(self):
        self.dizio = dictionary.Dictionary()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("______________________________")
        print("   Translator Alien-Italian")
        print("______________________________")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il Dizionario")
        print("5. Exit")
        print("______________________________\n")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        import re
        with open(dict, 'r', encoding="utf-8") as file:
            for riga in file:
                riga = riga.rstrip()
                riga = riga.lower()
                info = riga.split(" ",1)
                if re.search(r'[^a-zA-Z]', info[0]) or re.search(r'[^a-zA-Z]', info[1]):
                    ...
                else:
                    listaTraduzioni = info[1].split(" ")
                    self.dizio.addWord(info[0], listaTraduzioni)

    def handleAdd(self, entry: tuple):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        import re
        pAliena = entry[0]
        traduzioni = entry[1].split(" ")
        if re.search(r'[^a-zA-Z]', pAliena) or re.search(r'[^a-zA-Z\s]', entry[1]):
            print("Parola non aggiunta, non sono state seguite le regole sui caratteri")
        else:
            self.dizio.addWord(pAliena, traduzioni)
            print("Parola aggiunta!")

    def handleTranslate(self, query: str):
        # query is a string <parola_aliena>
        risultato = self.dizio.translate(query)
        return risultato

    def handleWildCard(self,query: str):
        # query is a string with a ? --> <par?la_aliena>
        risultato = self.dizio.translateWordWildCard(query)
        return risultato