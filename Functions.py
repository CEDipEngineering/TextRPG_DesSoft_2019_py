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
        'Carai',
        ['cima','baixo']
    ],
'Sala 1': [
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



