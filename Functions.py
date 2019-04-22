# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:51:49 2019
Fazer um jogo de RPG de texto estilo anos 80
@author: Carlos Dip & Edgard Ortiz
"""
import random 
from pprint import pprint
#from Main import Mapa
#from Main import Player
import time

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
def RunCombat(Player, Combat):
    Combat['Player']=Player # Coloca o jogador no dicionário
    fight_on=True
    mortos=[]
    pprint(Combat)
    while fight_on:
        for defunto in mortos:
            if defunto in Combat:
                del Combat[defunto]
        for combatant, attributes in Combat.items():
            if Combat[combatant]['Life']>0:
                print('Agora é o turno de ' + combatant)
                time.sleep(1)
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
        time.sleep(1)
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
        time.sleep(1)
        print(outputText)
    return None
#Recebe dois dicionários, um com os dados do atacante, e outro do atacado,
#seguidos de uma booleana que diz se é o player atacando.
#Retorna None, e imprime o resultado do ataque.

#%%
    
def Move(key, Mapa, Posicao, Player, Inventario):
    
    if key=='Voltar':
        if len(Posicao) > 1:
            Posicao.pop()
        key=Posicao[-1]
    elif key=='Pegar':
        key=Posicao[-1]
        AddInventario(key, Player, Inventario)
    elif key=='Terminal':
        if 'Chave' not in Inventario:
            print('Terminal trancado...insira sua chave.')
            return 1
        else:
            print('PARABÉNS! Vc é o único sobrevivente do nosso desafio.')
            return 0
    elif key=='PortaSecreta':
        AddInventario(key, Player, Inventario)
    elif key=='Quit':
        return 0
    elif key in Mapa:
        Posicao.append(key)
        if key=='Sala2':
            lista_monstros=[[100,5,'goblin'],[50,20,'tarantula'],[20,2,'rato']]
            luta=RunCombat(Player, CombatDict(lista_monstros))
            print(luta)
        elif key=='Sala3':
            lista_monstros=[[200,30,'Jason']]
            luta=RunCombat(Player, CombatDict(lista_monstros))
            print(luta)
    else:
        print('Comando inválido')
        return 1
    
    info=Mapa[key]
    print(info[0])
    time.sleep(1)
    print('Suas opções são {0}. (Coloque sua resposta exatamente como está escrito, ignorando espaços e o que estiver em parênteses)'.format(info[1]))
    
    return 1
  
#%%

def AddInventario(key, Player, Inventario):
    if key == 'Bau':
        if 'Baioneta' not in Inventario:
            Inventario.append('Baioneta')
            Player['Attack'] += 30 #30 de Attack adicionados
            print('A Baioneta é uma arma que aumenta o seu poder de ataque em 30 pts, isso deve te facilitar para os breves combates')
        else:
            print('Você já possui esse item!')
    
    elif key == 'Choque':
        if 'Chave' not in Inventario:
            Inventario.append('Chave')
            print('Agora você tem a chave, não deve encontrar mais nenhuma frustração quando achar a saída')
        else: 
            print('Aparentemente não há mais chaves por aqui...')
    
    elif key == 'PortaSecreta':
        if 'Wolverine' not in Inventario:
            Inventario.append('Wolverine')
            Player['Life'] += 100
            Player['Attack'] += 70
            print('Meu deus! Esse pequeno boneco trouxe benefícios na sua "Life" e poder de "Attack", você parece até um deus agora! Parabéns!')
        else:
            print('Ops...Não tem mais nada na sala dos... Ish... Quase falei, mas você tem que sair daqui, e rápido! Meu guerreiro...')
    
    return Inventario

#%%

#Posicao=[Mapa['CalabouçoInicial']]
#print(Posicao)
#x = Move(input())
#while Move(x)!=1:
#    x = Move(input())
#print(Posicao)
#lista_teste=[[100,5,'goblin'],[50,2,'criança'],[20,1,'rato']]
#teste=RunCombat(CombatDict(lista_teste))
#pprint(teste)
#  