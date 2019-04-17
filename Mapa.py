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
        ['Bau (Abre o baú no canto)',
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
        ['Sala3 (Avançar pela sala na direção da porta)',
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
        ['Sala3 (Avançar pela sala na direção da porta)',
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
        ['Sala3 (Avançar pela sala na direção da porta)',
         'Sala2 (Voltar)'],
    ],
'PortaSecreta': [
        '''
        Passando pela porta, você encontra uma sala
        muito estranaha, nela, todas as paredes são brancas,
        tão brancas que parecem até iluminadas,
        e sentado numa mesa no meio dessa sala, dois
        rapazes atrás de mesas, estão fazendo alguma coisa,
        cada um em seu laptop.
        Quando um deles te percebe, ele diz para o outro,
        num tom de sussurro, "Ei Dip, acho que alguém escapou...",        
        E o outro responde, sem nem olhar, "Pfft, você está brincando, Ed?
        Ninguém nunca coseguiu escap--" e antes de terminar sua frase,
        seu colega o empurra com o cotovelo, alertando-o. Ele então
        percebe sua presença, e um pouco desesperado, diz para você,
        "Ahhm.. Ah! Grande guerreiro! Você está só sonhando! Isso NÃO É REAL!
        Não se preocupe! Tudo vai ficar bem!" e ele tenta, sutilmente,
        avisar seu colega; "Rápido, tire ele daqui!", e o outro colega responde,
        "Mas para onde eu o mando?", e rapidamente é respondido "Sei lá, só mande
        ele pra longe daqui!", eles então percebem que você ainda está lá, e que
        agora está ficando um pouco impaciente, e então eles dizem, "Feroz, ehhhh... ,lutador,
        conquistador de, hmm... ahhmm... mutantes!, ehhhhh...., tome aqui esse objeto mágico que
        faz alguma coisa legal!", e ele toma da mesa uma miniatura de plástico humanóide, estranha,
        e quando o faz, seu colega diz "Eeeeiii! Esse é meu action figure do Wolverine! Você sabe
        quanto isso custou!?" e o outro responde com um rápido "Cala a boca, você quer que ele nos
        mate!?" ele então, vira-se para você e diz: "Poderoso guerreiro, agora, continue em sua busca,
        , por favor, só não nos machuque".
        Eles então, o entregam essa miniatura de hominídeo, e você sente, suas feridas se fecham,
        em frente a seus próprios olhos! Incrível!
        ''',
        [],
    ],
'Sala3': [
        '''
        Entrando por essa porta, você chega num grande salão, nele, você vê uma enorme linha
        de produção, agora há muito desativada, com centenas de peças diferentes espalhadas por
        esteiras que dão voltas e voltas, como as entranhas de uma gigantesca fera mecânica.
        No fundo da sala, você vê um terminal, ainda acesso, e uma escada, para o topo da fábrica.
        ''',
        ['Escada (Subir escada)',
         'Terminal (Acessar terminal)',
         'Radiacao (Abre a porta para a sala da radiação)',
         'Acido (Abre a porta para a sala do ácido)',
         'Choque (Abre a porta para a sala do choque)'],
    ],
'Bau': [
        '''
        O baú é velho e enrustido. Ao abrí-lo, você
        vê uma velha baioneta russa, usada na quarta guerra mundial,
        e uma carta, que diz "É perigoso ir sozinho. Leve isso.".
        ''',
        ['Abrir a porta',
         'Voltar'],
    ],
}
#pprint(Mapa)



