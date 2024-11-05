# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:07:27 2024

@author: kim.arne
"""
import sys

#Konstanter og beregninger k_ = konstanter
k_ELForsikring = 5000
k_BenzForsikring = 7500 
k_Trafikkforsikring = 8.38
k_Elforsikring_total = k_ELForsikring + (k_Trafikkforsikring * 365) #Total frosikringskostand elbil. antar ikke skuddår
k_BenzForsikring_total = k_BenzForsikring + (k_Trafikkforsikring * 365)#Total frosikringskostand bensinbil antar ikke skuddår
k_Strømpris_kWh = 2.0 
k_Drifstoff_EL = 0.2 * k_Strømpris_kWh #kostnad pr km elbil
k_Drifstoff_Benz = 1.0 #kostnad 

k_Bomavgift_el = 0.1
k_bomavgift_benz = 0.3



print("Enkel PY1010-1-24H Oppgave 1 Kim Arne Helle ")
print("Beregner utgiftene og sammenlikner årlige kostnadene ved bruk av elbil kontra bensinbil")

# Funksjoner
def hentkm(): #Henter data i funksjon for evt flere iterasjoner
 global kjørelengde #bruker kjørelengde globalt
 try:
    kjørelengde = int(input("Hva er din antatte kjørelengde i km: "))
    print("Du har tastet ",kjørelengde, "km")
    #else:#Ikke gyldig tall
 except ValueError:
     print("Inntastet verdi er ikke riktig. Prøv på nytt")
     hentkm()#ber bruker taste inn på nytt ved feil


def Totkost_elbil(km):
    statkost = k_Elforsikring_total
    varkost = (km * k_Drifstoff_EL) + (km * k_Bomavgift_el)
    totkost = int(statkost + varkost) #Bryr oss ikke om desimaler
    return (totkost)

def Totkost_benz(km):
    statkost = k_BenzForsikring_total
    varkost = (km * k_Drifstoff_Benz) + (km * k_bomavgift_benz)
    totkost = int(statkost + varkost) #Bryr oss ikke om desimaler
    return (totkost)
def presentasjon():  
#presentasjon
 print("Årlig kostnaden for ulike biltyper")
 print("Elbil faste kostnader: ", int(k_Elforsikring_total))
 print("Elbil totalkostnad i henhold til kjørelengde: ",Totkost_elbil(kjørelengde))
 #bensinbil
 print("Bensinbil faste kostnader: ",int(k_BenzForsikring_total))
 print("Bensinbil totalkostander i henhold til kjørelengde: ",Totkost_benz(kjørelengde))

 if Totkost_benz(kjørelengde) > Totkost_elbil(kjørelengde):
    print("Bensin er dyrest i henhold til kjørelengde")
    print("Du sparer :",(Totkost_benz(kjørelengde - Totkost_elbil(kjørelengde))), "kr på å kjøre elbil")
 else: #lite sansynlig men tar det med i tilfelle forholdene endrer seg.
  print("Elbil er dyrest i henhold til kjørelengde")
  print("Du sparer :",(Totkost_elbil(kjørelengde - Totkost_benz(kjørelengde ))), "kr på å kjøre bensinbil")
 
def avslutt(): #Avslutte eller kjøre en gang til
 svar = input("Vil du prøve igjen med flere tall ? J for ja eller trykk enter for avslutt: ")
 if svar.lower() == "j":
    hentkm()
    presentasjon()
    avslutt()  
 else:
     sys.exit(0)
#Funksjoner ferdig 

#Kjøreliste   
#Ber bruker taste inn kjørelengde i km
hentkm()  
presentasjon()
avslutt()


    
    











