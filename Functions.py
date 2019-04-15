# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:51:49 2019
Fazer um jogo de RPG de texto estilo anos 80
@author: Carlos Dip
"""
import random 
from pprint import pprint
from Mapa import Mapa
from Main import Player

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
    mortos=[]
    while fight_on:
        for defunto in mortos:
            if defunto in Combat:
                del Combat[defunto]
        for combatant, attributes in Combat.items():
            if Combat[combatant]['Life']>0:
                print('Agora é o turno de ' + combatant)
                #Player Turn
                if combatant == 'Player' and Player['Life']>0:
                    pprint(Combat)
                    ask=input('Quer atacar ou fugir? ')
                    # Fugir!
                    if ask == 'fugir':
                        if RollNum()>=11:
                            fight_on=False
                            return 'Você escapou!'
                        else:
                            print('Você não conseguiu escapar!')
                    
                    
                    #Não fugir!
                    else:
                        choose=True
                        while choose:
                            target=input('Quem você gostaria de atacar? ')
                            if target in Combat:
                                Attack(Combat['Player'] ,Combat[target], True)
                                choose=False
                            else:
                                print('Acho que você escreveu errado; Esse alvo não existe, ou já morreu!')
                                print('Tente escolher de novo.')
                #Monster Turn
                if combatant != 'Player':
                    Roll=RollNum()
                    if Roll>=5:
                        print(combatant + ' decidiu atacar você!')
                        Attack(Combat[combatant],Combat['Player'],False)
                    else:
                        print('{0} está confuso e passou seu turno procurando alguma coisa para fazer!'.format(combatant))
            else:
                mortos.append(combatant)
                
#Recebe um dicionário de combate (ver CombatDict), e então roda o combate, 
#até que todos os monstros morram, o player morra, ou o player fuja.  

#%%
#Função responsável pela ação de atacar.
def Attack(Attacker, Target, is_player):
    Roll=RollNum()
    if is_player:
        if Roll==20: # Acerto Crítico!
            Target['Life']-=2*Attacker['Attack']
            outputText=  'Seu rolamento foi ' + str(Roll) + 'e teve um acerto crítico, causando ' + str(2*Attacker['Attack']) + ' de dano!' 
        elif Roll>5: # Acerto normal
            Target['Life']-=Attacker['Attack']
            outputText='Seu rolamento foi ' + str(Roll) + ' causando ' + str(Attacker['Attack']) + ' de dano!' 
        else: #Erro
            outputText='Seu alvo desviou!'
        print(outputText)
    else:
        if Roll==20: # Acerto Crítico!
            Target['Life']-=2*Attacker['Attack']
            outputText=  'O rolamento dele foi ' + str(Roll) + 'e teve um acerto crítico, causando ' + str(2*Attacker['Attack']) + ' de dano!' 
        elif Roll>10: # Acerto normal
            Target['Life']-=Attacker['Attack']
            outputText='O rolamento dele foi ' + str(Roll) + ' causando ' + str(Attacker['Attack']) + ' de dano!' 
        else: #Erro
            outputText='Você desviou!'
        print(outputText)
    return None
#Recebe dois dicionários, um com os dados do atacante, e outro do atacado,
#seguidos de uma booleana que diz se é o player atacando.
#Retorna None, e imprime o resultado do ataque.

#%%
    
def Move(key):
    position=Mapa[key]
    print(position[0])
    print('Suas opções são {0}'.format(position[1]))
    return None


#%%
#lista_teste=[[100,5,'goblin'],[50,2,'criança'],[20,1,'rato']]
#teste=RunCombat(CombatDict(lista_teste))
#pprint(teste)
#    

    



