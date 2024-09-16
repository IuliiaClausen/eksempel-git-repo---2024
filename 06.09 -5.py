# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:49:40 2024

@author: 47925
"""

import turtle
import math

def tegn_trekant(n, vinkel_grad):
    vinkel_rad = math.radians(vinkel_grad)  
    # Konverterer graden til radianer

    # Beregn lengdene på hypotenus og motsatt katet
    hypotenus = n / math.cos(vinkel_rad)
    motsatt = n * math.tan(vinkel_rad)

    
    t = turtle.Turtle()

    t.forward(n)

    t.left(180 - vinkel_grad) 
    t.forward(hypotenus)

    t.left(90 + vinkel_grad) 
    t.forward(motsatt)

    turtle.done()

# Input fra bruker
n = float(input("Skriv inn lengden på linja langs x-aksen (n): "))
vinkel_grad = float(input("Skriv inn vinkelen mellom linja langs x-aksen og hypotenusen: "))

tegn_trekant(n, vinkel_grad)


