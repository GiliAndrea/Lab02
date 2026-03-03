class Translator:

    def __init__(self):
        self.dizio = {}

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
                riga.rstrip("\n")
                riga.lower()
                info = riga.split(" ")
                if re.search(r'[^a-zA-Z]', info[0]) and re.search(r'[^a-zA-Z]', info[1]):
                    ...
                else:
                    if info[0] not in self.dizio.keys():
                        self.dizio[info[0]] = []
                        self.dizio[info[0]].append(info[1])
                        tuplaTemp = tuple(self.dizio[info[0]])
                        self.dizio[info[0]] = list(tuplaTemp)
                    else:
                        self.dizio[info[0]].append(info[1])
                        tuplaTemp = tuple(self.dizio[info[0]])
                        self.dizio[info[0]] = list(tuplaTemp)

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if query in self.dizio.keys():
            risultato = self.dizio[query]
            print(risultato)
        else:
            print("Non è presente la traduzione")


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass