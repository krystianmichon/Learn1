# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:09:55 2019

@author: pc
"""

print('Witaj w prostym kalkulatorze!')
a = int(input('Podaj pierwsza liczbe: '))
b = int(input('Podaj druga liczbe: '))
c = int(input('Wybierz rodzaj działania: 1 - dodawanie, 2-odejmowanie, 3 - mnozenie, 4 - dzielenie: ' ))

if(c==1):
    wynik = a + b
elif(c==2):
    wynik = a - b
elif(c==3):
    wynik = a * b
elif(c==4):
    wynik = a / b

else:
    print('Dokonales zlego wyboru!')
    
print('Wynik dzialania to: ', wynik)