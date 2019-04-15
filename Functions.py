# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:51:49 2019
Fazer um jogo de RPG de texto estilo anos 80
@author: Carlos Dip
"""
import random 
from pprint import pprint

#%%

#Funcão para rolar um D20
def RollNum():
    return random.randint(1,20)
#Não tem entradas, returna diretamente um número inteiro de 1 a 20 (inclusivo)
#%%

#Funcão para criar um monstro, dados sua vida, dano por golpe e identificador.
def CreateMonster(Life,Attack):
    Monster={
        'Attack':Attack,
        'Life':Life
    }   
    return Monster
#Entra 2 atributos, Life e Attack de um monstro. Em seguida cria um dicionário, com os atributos do monstro, e o retorna. 

#%%

#Função para iniciar dicionário de combate. 
def CombatDict(ListAttrMonsters):  
    Combat=dict()
    for index,monster in enumerate(ListAttrMonsters): #Loop para criar monstros e colocá-los no dicionário Combat.
        this_monster=ListAttrMonsters[index]
        Life=this_monster[0]
        Attack=this_monster[1]
        id_=this_monster[2]
        Combat[id_]=CreateMonster(Life,Attack)
    return Combat
#Entra uma lista contendo listas, as quais possuem, em ordem, a vida, dano e identificador de um monstro. Para cada lista dentro da principal, será criado um monstro.
#Cada monstro é colocado num dicionário, que é retornado.

#%%

#Função para rodar o combate.
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
        
#Recebe um dicionário de combate (ver CombatDict), e então roda o combate, 
#até que todos os monstros morram, o player morra, ou o player fuja.  

#%%
#Função responsável pela ação de atacar.
def Attack(Attacker, Target):
    Roll=RollNum()
    if Roll==20: # Acerto Crítico!
        Target['Life']-=2*Attacker['Attack']
        outputText= Attacker + ' rolou ' + str(Roll) + 'e teve um acerto crítico, causando ' + str(2*Attacker['Attack']) + 'de dano!' 
    elif Roll>10: # Acerto normal
        Target['Life']-=Attacker['Attack']
        outputText=Attacker + ' rolou ' + str(Roll) + 'e teve um acerto crítico, causando ' + str(Attacker['Attack']) + 'de dano!' 
    else: #Erro
        outputText=Attacker + ' errou!'
    if Target['Life']<=0 and Target!='Player': #Se o alvo morreu
        del Combat[Target]
    return outputText
#Recebe duas Strings, uma é o atacante, e outra o atacado, e ambas são chaves no dicionário de combate.
#Retorna o resultado da tentativa de ataque.

#%%
#lista_teste=[[100,5,'goblin'],[50,2,'criança'],[20,1,'rato']]
#pprint(CombatDict(lista_teste))
    



