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

    def translateWordWildCard(self, query: str):
        import string
        risultato = []
        listaCaratteri = list(string.ascii_lowercase)
        giolli = query
        for c in listaCaratteri:
            giolli = giolli.replace("?", f"{c}")
            if giolli in self.dizio.keys():
                risultato = risultato + self.dizio[giolli]
            giolli = query
        return risultato

    def stampaTot(self):
        for e in self.dizio.keys():
            print(f"Parola aliena: {e} - traduzione: {self.dizio[e]}")