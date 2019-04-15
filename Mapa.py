# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:51:49 2019
Fazer um jogo de RPG de texto estilo anos 80
@author: Carlos Dip
"""
#Mapa onde o jogo acontece. Fácilmente expandido,
#formato:
#Mapa={
# 'Nome do lugar': [
#   '''Descrição do lugar, e de algumas possiveis
#   opcoes''',
#   [opções]
#]
#}
import json
from pprint import pprint

Mapa = {
'CalabouçoInicial': [
        '''
        Você está num calabouço, escuro e úmido. 
        Não consegue ver muito longe.
        Está com fome, e cansado.
        Não se lembra como chegou aqui,
        tudo que sabe, é seu nome, e que
        algo, ou alguém o trouxe para cá.
        Conforme recobra consciência, percebe
        que suas mãos estão atadas.
        Sem muito esforço, consegue libertar-se
        de suas amarras e levantar-se.
        ''',
        {'Examinar': '''
         Parece que há um baú de madeira no canto da sala.
         As paredes são de pedra lisa, e você consegue ouvir
         água gotejando no canto. De vez em quando ouve um rato
         correndo por algum canto.
         Há também uma porta de madeira meio enferujada 
         entreaberta, que parece uma possível saída.
         ''',
         'Olhar baú':'''
         Examine o baú no canto da sala.
         ''',
         'Sair pela porta':'''
         Sair pela porta, e descobrir o que o aguarda
         fora desta sala imunda.
         '''}
    ],
'Calabouço': [
        'Carai',
        ['cima','baixo']
    ],
'Sala 2': [
        'Carai',
        ['cima','baixo']
    ],
'Sala 3': [
        'Carai',
        ['cima','baixo']
    ],
'Sala 4': [
        'Carai',
        ['cima','baixo']
    ],
'Sala 5': [
        'Carai',
        ['cima','baixo']
    ],
'Sala 6': [
        'Carai',
        ['cima','baixo']
    ],
'Sala 7': [
        'Carai',
        ['cima','baixo']
    ],
'Sala 8': [
        'Carai',
        ['cima','baixo']
    ],
}
pprint(Mapa)



