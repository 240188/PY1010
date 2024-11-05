# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:15:40 2024

@author: kim.arne
"""

#Oppgave 4 a)
data = {
        "Norge": ["Oslo",0.634],
        "England": ["london",8.982],
        "Frankrike": ["Paris",2.873],
        "Italia": ["Roma",2.873]
        }


#Oppgave 4 c
def ikkefunnet():
    #Litt unødvendig å be om navnet to ganger men for å oppfulle arbeidskravet så gjør jeg det slik
    nyttland = input("Landet var ikke i boken. Tast inn navnet på landet: ")
    hovedstad = input("Skriv inn hovedstaden du kan også oppdatere land som ligger i katalogen: ")
    innbyggere = input("Skriv inn antall innbyggere i milioner: ")
    data.update({nyttland:[hovedstad, innbyggere]})
    print("\n","Data er oppdatert,")
    print("Liste over land i katalogen")
    
    #Skriver ut i listeform med et land pr linje for å gjøre det lettere å lese
    for x in data:
        print("Land:", x, "hovedstad:",data[x][0], " innbyggertall:", data[x][1])
    
    



#Oppgave 4 b)
print("Liste over ulike navn med hovedstad og innbyggertall \n")
Let_land = input("Skriv inn et land: ")

#Eksempel på teksten som skal stå
#London er hovedstaden i England og det er 8.982 mill. innbyggere i London



#sjekker om nøkkelv er i dict og ber bruker taste inn nytt land
if data.get(Let_land, 0) == 0:
  ikkefunnet()
else:print(data[Let_land][0],"er hovedstaden i",Let_land, "og det er ",data[Let_land][1], " mill. innbyggere i",Let_land)
    
    




    
    
    


