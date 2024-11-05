# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 08:29:21 2024

@author: kim.arne
"""
import matplotlib.pyplot as plt
import numpy as np

#Oppgavetekst:
#Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10].
#Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet
#[-10,10].

plt.style.use('_mpl-gallery') #Liker denne stilen
#plt.style.use('ggplot')

#Data for plottet
x = np.linspace(-10, 10, 200) #Definere X aksen
y = pow(-x,2) -5 #Y aksen verdier


# plot data
#Det er ikke oppgitt enheter i oppgaven så verdier er enhetsløse
fig, ax = plt.subplots()
ax.set_title("Arbeidskrav 2 oppgave 6", fontsize=10)
ax.plot(x, y, linewidth=1)
plt.show()


