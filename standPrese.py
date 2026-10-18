from stand import Stand


class StandPrese(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(codice,superficie,padiglione,prezzo_base)
        self._numero_prese=numero_prese

    def calcola_prezzo(self):
        return self._prezzo_base*(1+0.07*self._numero_prese)

    def __str__(self):
        return f"{self._codice}: Prese Extra | {self._superficie} mq - Padiglione {self._padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - Prese: {self._numero_prese}"
