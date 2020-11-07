#! /usr/bin/env python3

########################
###      CLASSE      ###
########################


class Gatto():
    verso = 'Miao'
    russare = 'prrr prrr'

    def miagolare(self):
        print(self.verso)
    
    def dormire(self):
        print(self.russare)

def main():
    pallina = Gatto()
    print(pallina.verso)

if __name__ == "__main__":
    main()

