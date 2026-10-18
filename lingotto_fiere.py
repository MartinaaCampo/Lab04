import csv

from espositore import Espositore
from stand import Stand
from standPremium import StandPremium
from standPrese import StandPrese


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome=nome
        self._stands=[]
        self.espositori=[]
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nuovo_nome):
        self._nome=nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path,'r',encoding='utf8') as f:
                reader = csv.reader(f)
                for riga in reader:
                    riga=[item.strip() for item in riga]
                    if not riga or not riga[0]:
                        continue
                    codice=riga[0]
                    if codice.startswith('ST'):
                        superficie=float(riga[1])
                        padiglione=int(riga[2])
                        prezzo_base=float(riga[3])
                        if len(riga)==4 or len(riga)==5 and riga[4]=="<unset>":
                            stand=Stand(codice,superficie,padiglione,prezzo_base)
                        elif len(riga)==5:
                            extra=riga[4]
                            if extra.isdigit():
                                stand=StandPrese(codice,superficie,padiglione,prezzo_base,int(extra))
                            else:
                                stand=StandPremium(codice,superficie,padiglione,prezzo_base,extra)
                        self._stands.append(stand)
                    elif codice.startswith('ES'):
                        nome=riga[1]
                        cognome=riga[2]
                        espositore=Espositore(codice,nome, cognome)
                        self.espositori.append(espositore)
        except FileNotFoundError:
            print("errore: file non trovato")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        stand_trovato=None
        for s in self._stands:
           if s.codice_stand==codice_stand:
               stand_trovato=s
               break
        if not stand_trovato:
            print(f"errore: {codice_stand} non trovato")
        espositore_trovato = None
        for e in self.espositori:
            if e.codice_espositore == codice_espositore:
                espositore_trovato = e
                break
        if not espositore_trovato:
            print(f"errore: {codice_espositore} non trovato")

        espositore_trovato.stand_assegnato = stand_trovato

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        if not self.espositori:
            print("Nessun espositore registrato.")
            return

        for espositore in self.espositori:
            print(espositore)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self._stands)
