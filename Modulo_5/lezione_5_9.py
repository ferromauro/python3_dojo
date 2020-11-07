#! /usr/bin/env python3

#########################################
###      POLIMORFISMO CON FUNZIONE    ###
#########################################


# Polimorfismo in Python
class Cane:

    def miagola(self):
        print("Il mio cane non miagola")

class Gatto:

    def miagola(self):
        print("Il mio gatto miagola")

# interfaccia comune
def evento(animale):
    animale.miagola()

# istanza oggetto
tyson = Cane()
pallina = Gatto()

# passaggio degli oggetto all'interfaccia comune
evento(tyson)
evento(pallina)
