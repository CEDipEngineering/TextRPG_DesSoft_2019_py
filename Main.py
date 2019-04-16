# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:51:49 2019
Fazer um jogo de RPG de texto estilo anos 80
@author: Carlos Dip
"""
import Functions as fn
from Mapa import Mapa

Player = {
    'Life':200,
    'Attack':20        
}
ask=input('Bem-vindo! Quer começar a jogar (s/n)? ')
game_on = ask == 's'
if not game_on:
    print('Ok, até a próxima! ')
if game_on:
    PlayerName=input('Sábia escolha! Qual seu nome? ')
    print('Bem vindo, {0}, à maior aventura de sua vida!'.format(PlayerName))
    position=[]
    fn.Move('CalabouçoInicial')
#    while game_on:
#        
#        break