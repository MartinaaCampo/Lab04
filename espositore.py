class Espositore:
    def __init__(self,codice,nome,cognome):
        self._codice = codice
        self._nome = nome
        self._cognome = cognome
        self._stand_assegnato = None

    @property
    def codice(self):
        return self._codice
    @property
    def stand_assegnato(self):
        return self._stand_assegnato

    @stand_assegnato.setter
    def stand_assegnato(self, stand):
        self._stand_assegnato = stand

    def __eq__(self, other):
        if isinstance(other, Espositore):
            return self._codice == other.codice
        return False

    def __str__(self):
        stand_info = self._stand_assegnato.codice if self._stand_assegnato else "Nessuno"
        return f"Espositore {self._codice}: {self._nome} {self._cognome} - Stand: {stand_info}"