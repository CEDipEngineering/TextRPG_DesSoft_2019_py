# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:51:49 2019
Fazer um jogo de RPG de texto estilo anos 80
@author: Edgard Ortiz & Carlos Dip
"""
import Functions as fn
from pprint import pprint
import json
with open('Mapa.txt','r') as Map:
    conteudo=Map.read()
    
#variaveis globais  
Player = {
    'Life':150,
    'Attack':5        
}

Inventario=[]
Posicao=[]
Mapa=json.loads(conteudo)

#game
ask=input('Bem-vindo! Quer começar a jogar (s/n)? ')
 
if ask=='s':
    PlayerName=input('Sábia escolha! Qual seu nome? ')
    print('Bem vindo, {0}, à maior aventura de sua vida!'.format(PlayerName))
    game_on = fn.Move('CalabouçoInicial', Mapa, Posicao, Player, Inventario)
    while game_on:
        key=input('Digite sua opção:')
        game_on = fn.Move(key, Mapa, Posicao, Player, Inventario)

print('Ok, até a próxima! ')