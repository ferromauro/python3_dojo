#! /usr/bin/env python3

###############################
###      EREDITARIETA'      ###
###############################

class Animale:
    def __init__(self, name, sound):
        self._name = name
        self._sound = sound
        print('Ho creato un animale')

    def restituisci_nome(self):
        print(self._name)
        
    def sound(self):
        print(self._sound)

class Gatto(Animale):
    def __init__(self, name, sound, action):
        super().__init__(name,sound)
        print('Ho creato un GATTO!')
        self._action = action
        
    def agisci(self):
        print(self._action)
    
def main():
    #x = Animale('Bingo', 'Bau!')
    #x.restituisci_nome()
    #x.sound()    

    y = Gatto('Pallina', 'Miao', 'Graffia')
    y.restituisci_nome()
    y.sound()   
    y.agisci()

if __name__ == "__main__":
    main()


