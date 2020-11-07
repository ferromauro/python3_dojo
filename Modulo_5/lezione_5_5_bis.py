#! /usr/bin/env python3

#######################################
###      COSTRUTTORE DI CLASSE      ###
#######################################

class Animale:
    def __init__(self,**kwargs):
        self._family = kwargs['family']  if 'family' in kwargs else 'felini'
        self._name =   kwargs['name']    if 'name' in kwargs else 'Pallina'
        self._sound =  kwargs['sound']   if 'sound' in kwargs else 'Miao'
    
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
    cane = Animale(name='Snoopy', family='canidi', sound='bau bau')
    print_animal(cane)
    gatto = Animale()
    print_animal(gatto)

if __name__ == "__main__":
    main()
