#! /usr/bin/env python3

######################################
###      POLIMORFISMO DI BASE      ###
######################################

# Definisco classe di base
class Animale:
    def __init__(self, nome):
        self.nome = nome

# Definisco prima classe figlia        
class Gatto(Animale):
   def failverso(self):
       return 'Miao'

# Seconda classe figlia       
class Cane(Animale):
   def failverso(self):
       return 'Bau'

# Creo delle istanze delle classi figlie       
a = Gatto('Fufi')
b = Gatto('Ciccio')
c = Cane('Fido')

# Posso iterare gli elementi di una lista andando a chiamare la funzione corretta per ogni istanza.
for animale in [a, b, c]:
    print(f'{animale.nome}: {animale.failverso()}')