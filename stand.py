class Stand:
    def __init__(self,codice,superficie,padiglione,prezzo_base):
        self._codice=codice
        self._superficie=superficie
        self._padiglione=padiglione
        self._prezzo_base=prezzo_base

    @property
    def codice(self):
        return self._codice
    def calcola_prezzo(self):
        return self._prezzo_base

    def __eq__(self, other):
        if isinstance(other,Stand):
            return self._codice==other._codice
        return False

    def __lt__(self, other):
        if isinstance(other, Stand):
            return self.calcola_prezzo() < other.calcola_prezzo()
        return NotImplemented
    def __str__(self):
        return  f"{self._codice}: Standard | {self._superficie} mq - Padiglione {self._padiglione} - Prezzo {self.calcola_prezzo():.2f}€"


