# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:51:49 2019
Fazer um jogo de RPG de texto estilo anos 80
@author: Carlos Dip & Edgard Ortiz
"""
import Functions as fn
from pprint import pprint
import json
with open('Mapa.txt','r') as Map:
    conteudo=Map.read()
    Mapa=json.loads(conteudo)
#pprint(Mapa)
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
#inventário:
inventario = []
Itens = ['Baioneta', 'Chave', 'Wolverine']
for e in Itens:
    inventario.append(e)
    if 'Baioneta' in inventario:
        Player['Attack'] = 50 #30 de Attack adicionados
    if 'Chave' in inventario:
        True
    if 'Wolverine' in inventario:
        Player['Life'] = 300
        Player['Attack'] = 100
    