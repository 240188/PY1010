# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:34:43 2024

@author: kim.arne
"""
import numpy as np #def pi
import math

#Oppgavetekst fra arbeidskrav 2 oppg 5
#Lag et program med en funksjon som tar a og b som inn-argumenter og som så
#regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en
#halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
#Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
#tekst.


print("Programmet beregner areal og omkrets av en halvsirkel og rettvinklet trektant i en sammensatt figur")
a = float(input("Skriv inn diameter av halvsirkelen i cm : "))
b = float(input("Skriv inn høyden på den retviklede trekanten i cm: "))

#Halvsirkel areal. Deler på 2.
A_halvsirkel = (pow((a/2),2) * np.pi)/2
print(A_halvsirkel)

#Omkrets halvsirkel. Sløyfer å gange med 2 siden vi uasett skulle dele på 2
O_halvsirkel = np.pi * (a/2)
print("Omkrets halvsirkel: ",O_halvsirkel, "cm")

#Areal rettviklet trekant
A_trekant = (a*b)/2
print ("Areal av trekant: ",A_trekant, "cm^2")

#Omkrets trekant minus grunnflate siden denne ikke er med i ytre omkrets
hypotetnus = math.sqrt(pow(b,2) + pow(a,2)) #pytogoras setning for å finne hypotenus
O_Trekant = b + hypotetnus;
print("Ytre omkrets trekant: ",O_Trekant, "cm")

#Total areal
A_tot = A_halvsirkel + A_trekant
print("Areal av halvsirkel og rettvinklet trekant er :", A_tot," cm^2")

#Ytre omkrets
O_tot = O_halvsirkel + O_Trekant
print("Ytre omkrets av halvsikrel og rettvinklet trekant er :",O_tot, "cm")