class Translator:

    def __init__(self):
        self.dizio = {}

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("______________________________\n")
        print("   Translator Alien-Italian\n")
        print("______________________________\n")
        print("1. Aggiungi nuova parola\n")
        print("2. Cerca una traduzione\n")
        print("3. Cerca con wildcard\n")
        print("4. Stampa tutto il Dizionario\n")
        print("5. Exit\n")
        print("______________________________\n\n")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        import re
        with open(dict, 'r', encoding="utf-8") as file:
            for riga in file:
                riga.strip()
                riga.lower()
                info = riga.split(" ")
                if re.search(r'[^a-zA-Z]', info[0]) and re.search(r'[^a-zA-Z]', info[1]):
                    ...
                else:
                    if info[0] in self.dizio.keys():
                        self.dizio[info[0]] = []
                        self.dizio[info[0]].append(info[1])
                    else:
                        self.dizio[info[0]].append(info[1])

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass