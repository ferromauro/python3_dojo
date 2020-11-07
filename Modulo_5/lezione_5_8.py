#! /usr/bin/env python3

#####################################
###        GETTER & SETTER        ###
#####################################

class Utente:
    def __init__(self,**kwargs):
        self.__age =   kwargs['age']   
        
    def get_age(self):
        return self.__age
    
    def set_age(self, x):
        self.__age = x if x > 18 else print('Devi essere maggiorenne')
    
def print_data(x):
    if not isinstance(x,Utente):
        raise TypeError('print_data: richiede un oggetto Utente()')
    print(f'L\'utente ha {x.get_age()} anni.')

def main():
    user_one = Utente(age=22)
    print_data(user_one)
    user_one.set_age(-22)
    print_data(user_one)
    
    #user_one.__age(-2)
    #print_data(user_one)


if __name__ == "__main__":
    main()
