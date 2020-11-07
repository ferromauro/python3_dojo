#! /usr/bin/env python3

#####################################
###        INCAPSULAMENTO        ###
#####################################
# Incapsulamento in Python
class Auto:

    def __init__(self):
        self.__colore = "verde"

    def colora(self):
        print(f"La mia auto è di colore {self.__colore}")

    def impostaColore(self, variante):
        self.__colore = variante

# istanza di classe
x = Auto()
x.colora()

# modifica del colore
x.__colore = "rosso"
x.colora()

# funzione setter
x.impostaColore("rosso")
x.colora()
