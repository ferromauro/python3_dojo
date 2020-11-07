#! /usr/bin/env python3

#######################################
###      COSTRUTTORE DI CLASSE      ###
#######################################

class Animale:
    def __init__(self,name, family, sound):
        self._family = family
        self._name = name
        self._sound = sound
    
    def family(self):
        return self._family
    
    def name(self):
        return self._name
        
    def sound(self):
        return self._sound
        
def print_animal(el):
    if not isinstance(el,Animale):
        raise TypeError('print_animal: richiede un oggetto Animale()')
    print(f'L\'animale {el.name()} appartiene alla famiglia dei {el.family()} e fa {el.sound()}!')

def main():
    gatto = Animale('Pallina', 'felini', 'miao')
    leone = Animale('Ercole', 'felini', 'roar')
    print_animal(gatto)
    print_animal(leone)

if __name__ == "__main__":
    main()
