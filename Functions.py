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
import random 
from pprint import pprint

#%%
#Funcão para rolar um D20
def RollNum():
    return random.randint(0,20)

#%%

#Funcão para criar um monstro, dados sua vida, dano por golpe e identificador.
def CreateMonster(Life,Attack):
    Monster={
        'Attack':Attack,
        'Life':Life
    }   
    return Monster

#%%

#ListAttrMonsters = Lista de dimensões NumMonsters x 3, 
#onde cada elemento consiste na vida e attack de cada monstro, seguido de seu id
#como em [100, 8, 'Goblin 1'], cria-se um monstro, chamado Goblin 1, com 100 de vida e 8 de dano. 
def CombatDict(ListAttrMonsters):  
    Combat=dict()
    for index,monster in enumerate(ListAttrMonsters): #Loop para criar monstros e colocá-los no dicionário Combat.
        this_monster=ListAttrMonsters[index]
        Life=this_monster[0]
        Attack=this_monster[1]
        id_=this_monster[2]
        Combat[id_]=CreateMonster(Life,Attack)
    return Combat

#%%

#Função que recebe um dicionário de combate (ver CombatDict), e então roda o combate, 
#até que todos os monstros morram, o player morra, ou o player fuja.
def RunCombat(Combat):
    Combat['Player']=Player # Coloca o jogador no dicionário
    fight_on=True
    while fight_on:
        for combatant, attributes in Combat.items():
            
            #Player Turn
            if combatant == 'Player':
                ask=input('Quer atacar ou fugir? ')
                
                # Fugir!
                if ask == 'fugir':
                    if RollNum()>=11:
                        fight_on=False
                        break
                    else:
                        print('Você não conseguiu escapar!')
                
                
                #Não fugir!
                elif len(Combat)>2: #Se o jogador não está lutando com só um monstro:
                    target=input('Quem você gostaria de atacar? ')
                    if target in Combat:
                        Attack(Combat[Player],Combat[target])
                else:
                    k=Combat.keys()
                    k.remove('Player')
                    Attack(Combat[Player],k)
        
    

#%%
def Attack(Attacker, Target):
    Roll=RollNum()
    if Roll==20: # Acerto Crítico!
        Target['Life']-=2*Attacker['Attack']
        outputText='Você rolou ' + str(Roll) + 'e teve um acerto crítico, causando ' + str(2*Attacker['Attack']) + 'de dano!' 
    elif Roll>10: # Acerto normal
        Target['Life']-=Attacker['Attack']
        outputText='Você rolou ' + str(Roll) + 'e teve um acerto crítico, causando ' + str(Attacker['Attack']) + 'de dano!' 
    else: #Erro
        outputText='Você errou!'
        return outputText
                        

#%%
#lista_teste=[[100,5,'goblin'],[50,2,'criança'],[20,1,'rato']]
#pprint(CombatDict(lista_teste))
    



