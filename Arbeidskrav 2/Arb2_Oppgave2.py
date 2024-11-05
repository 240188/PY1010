# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:51:25 2024

@author: kim.arne
"""
import math #trenger .ceil funksjon
antall_elever = int(input('Skriv inn antall elever:' ))

#Konstanter
elevspiser = 0.25 #1/4 pizza pr elev

#Beregne antall pizzaer
Ant_Pizza= math.ceil(antall_elever * elevspiser) #Runder opp til nærmeste heltall

print("Om elevene spiser i snitt ", elevspiser, "pizaer så er det nødvendig å handle",int(Ant_Pizza), "pizzaer")
