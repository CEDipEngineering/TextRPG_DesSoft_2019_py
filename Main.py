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
line='--------------------------------------------------------------------------'
print(line)
print('Bem-vindo a uma aventura pós-apocalíptica russa.')
print('No ano 2177, o mundo está ainda devastado pelo fogo')
print('nuclear. Homens e mulheres andam por todo lugar,')
print('desfigurados pela radiação. O mundo está no fim.')
print('Ou, será um recomeço?')
print(line)

Inventario=[]
Posicao=[]
Mapa=json.loads(conteudo)

#game
ask=input('Bem-vindo! Quer começar a jogar (s/n)? ')
 
if ask=='s':
    regras='A qualquer momento, você pode escrever "Quit" (sem aspas) para sair do jogo. Sua vida começa em 150 e você causa 5 de dano com cada ataque'
    print(regras)
    PlayerName=input('Sábia escolha! Qual seu nome? ')
    print('Bem vindo, {0}, à maior aventura de sua vida!'.format(PlayerName))
    game_on = fn.Move('CalabouçoInicial', Mapa, Posicao, Player, Inventario)
    while game_on:
        key=input('Digite sua opção: ')
        bool_var = fn.Move(key, Mapa, Posicao, Player, Inventario)
        if bool_var==-1:
            key=input('Quer teleportar para onde? ')
            fn.Move(key,Mapa,Posicao,Player, Inventario)
        else:
            game_on=bool(bool_var)
            

print('Ok, até a próxima! ')
