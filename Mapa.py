# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:51:49 2019
Fazer um jogo de RPG de texto estilo anos 80
@author: Carlos Dip
"""
#Mapa onde o jogo acontece. Fácilmente expandido,
#formato:
#Mapa={
# 'Nome do lugar': ['''
#   Descrição do lugar
#''',
#   ['opção(descrição da opção)',
#    'opção(descrição da opção)']
#]
#}
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
        ['Examinar (A sala)',
         'Abrir_Bau',
         'Corredor1 (Abrir a porta)']
    ],
'Corredor1': [
        '''
        Agora saindo do calabouço, você se encontra
        num corredor estreito. Você segue ele até uma curva
        fechada para a direita. E então depara-se com uma
        porta metálica e pesada. Muito enferrujada.
        Nela está gravado:
            'Опасность.'
        O que será que isso significa?
        ''',
        ['Sala2 (Abrir a porta)',
         'CalabouçoInicial (Voltar)'],
    ],
'Sala2': [
        '''
        Agora livre dos seres mutantes estranhos, 
        você toma um momento para se acalmar.
        Esta sala estranha é toda de concreto.
        Nela, existem 3 portas. Todas de concreto.
        A primeira, a sua esquerda, tem um símbolo
        triangular amarelo, que você reconhece como
        relacionado a radiação.
        A segunda, à sua frente, tem um símbolo que você
        reconhece como de perigo de ácidos.
        E a terceira, à sua direita, você identifica como perigo de
        choque elétrico em alta tensão.
        ''',
         ['Radiacao (Abrir a porta da esquerda)',
         'Acido (Abrir a porta do centro) ',
         'Choque (Abrir a porta da direita)',
         'Corredor1 (Voltar)'],
    ],
'Radiacao': [
        '''
        Você encontra uma sala completamente destruída.
        Paredes cobertas por uma lama pesada e escura,
        você só consegue enxergar graças a uma leve fluorescência
        vindo de algumas formações rochosas azuis, parecidas com
        enormes stalagmites de diamante saindo do chão.
        A sala está fria e úmida. No fundo da sala você
        vê uma porta. Ela parece ser a saída.
        Porém entre você e a porta, existe um mar de rochas
        fluorescentes e lama.
        ''',
        ['Porta (Avançar pela sala na direção da porta)',
         'Fininho (Avançar com cuidado pelos cantos da sala na direção da porta)',
         'Sala2 (Voltar)'],
    ],
'Acido': [
        '''
        Ao abrir a porta, um cheiro muito poderoso o domina.
        Você não consegue resistir, e tosse incontrolavelmente por
        alguns instantes. Quando recobra seu fôlego, percebe que
        a sala em questão parece ser um tipo de chuveiro coletivo,
        onde dezenas de chuveiros estão escorrendo um líquido transparente,
        e levemente sujo. Você também observa que esse líquido parece ter
        propriedades corrosivas, visto que o entorno de seu caminho agora
        está escavado e afundado pelo que parece ter sido um fluxo incessante
        de ácido. Provavelmente não é uma boa ideia tocar nisso.
        Do outro lado, você vê uma porta de saída.
        ''',
        ['Porta (Avançar pela sala na direção da porta)',
         'Sala2 (Voltar)'],
    ],
'Choque': [
        '''
        Nesta sala, antes mesmo de abrir a porta, você
        percebe uma leve luz, vazando pelo entorno desta.
        Resoluto, você abre a porta, e vê, 
        o que te parece uma tespetade em primeiro olhar,
        mas na verdade não passam de bobinas de Tesla ativas.
        Dezenas delas. Tantas, que a sala parece estar iluminada
        somente pelos seus magníficos arcos elétricos.
        Tão belos quanto mortais.
        Ao fim da sala, parece haver uma porta de saída.
        ''',
        ['Porta (Avançar pela sala na direção da porta)',
         'Sala2 (Voltar)'],
    ],
'Sala 6': [
        '''
        ''',
        ['Abrir a porta',
         'Voltar'],
    ],
'Sala 7': [
        '''
        ''',
        ['Abrir a porta',
         'Voltar'],
    ],
'Sala 8': [
        '''
        ''',
        ['Abrir a porta',
         'Voltar'],
    ],
}
#pprint(Mapa)



