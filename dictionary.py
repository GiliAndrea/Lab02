class Dictionary:
    def __init__(self):
        self.dizio = {}

    def addWord(self, pAliena: str, traduzione: list[str]):
        if pAliena not in self.dizio.keys():
            self.dizio[pAliena] = []
            self.dizio[pAliena] = traduzione
        else:
            self.dizio[pAliena] = self.dizio[pAliena] + traduzione
            self.dizio[pAliena] = list(set(self.dizio[pAliena]))

    def translate(self, query: str):
        if query in self.dizio.keys():
            risultato = self.dizio[query]
            return risultato
        else:
            risultato = "Non è presente la traduzione"
            return risultato

    # queto lo lascio alla fine
    def translateWordWildCard(self):
        pass

    def stampaTot(self):
        for e in self.dizio.keys():
            print(f"Parola aliena: {e} - traduzione: {self.dizio[e]}")