import json
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
        Examinando a sala em seu entorno,
        percebe que há uma porta enferrujada e entreaberta,
        assim como um baú no canto da sala.
        ''',
        ['Bau (Vai até o baú no canto, e o abre)',
         'Corredor1 (Abrir a porta)']
    ],
'Corredor1': [
        '''
        Agora saindo do calabouço, você se encontra
        num corredor estreito. Você segue ele até uma curva
        fechada para a direita. E então depara-se com uma
        porta metálica e pesada. Muito enferrujada.
        Nela está gravado:
            'Opasnost'
        O que será que isso significa?
        ''',
        ['Sala2 (Abrir a porta)',
         'Voltar (CalabouçoInicial)'],
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
         'Voltar (Corredor1)'],
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
         'Voltar (Sala2)'],
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
         'Voltar (Sala2)'],
    ],
'Choque': [
        '''
        Nesta sala, antes mesmo de abrir a porta, você
        percebe uma leve luz, vazando pelo entorno desta.
        Resoluto, você abre a porta, e vê, 
        o que parece uma tempestade em primeiro olhar,
        mas na verdade não passam de bobinas de Tesla ativas.
        Dezenas delas. Tantas, que a sala parece estar iluminada
        somente pelos seus magníficos arcos elétricos.
        Tão belos quanto mortais. Porém, no meio de tantos perigos,
        surge uma esperança, em um canto mais escuro em baixo e no lado esquerdo
        do galpão, reflete um brilho. Sem hesitar, você se aproxima desse então 
        objeto brilhante e o mesmo, a cada vez mais que se aproxima,
        se revela uma chave, e perto dela há uma mensagem cravada na parede
        próxima: 'Ispol'zuy, chtoby vybrat'sya otsyuda', sem ter ideia do que 
        siginifica, você pode decidir guardá-la pois. Por que iriam escrever alguma coisa
        se não fosse importante?
        Ao fim da sala, parece haver uma porta de saída.
        ''',
        ['Pegar (Pegar chave)', 'Sala3 (Avançar pela sala na direção da porta)',
         'Voltar (Sala2)'],
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
        ['Pegar (Pegar baioneta)',
         'Voltar'],
    ],
'Escada': [
        '''
        Subindo a escada, você chega no topo da fábrica.
        Daí, você consegue ver uma cidade enorme em seu entorno.
        Toda em ruínas. De vez em quando passa um mutante correndo
        de uma lado para outro numa rua. Carros destruídos 
        populam a paisagem, agora recoberta por vegetação.
        Ao seu lado, um esqueleto, e na mão dele uma carta, que diz
        o seguinte: "Droga Michael, te disse para não me esperar.
        Agora olha o que foi acontecer. E a chave do terminal? Onde
        foi que você perdeu? Aposto que foi lá perto da sala 2.
        Em qual setor você trabalhava mesmo? Radiação, ou Choque?
        Nunca me lembro. Bom. Acho que é isso então. Não tem cara de 
        que vou sair daqui tão cedo, e não estou nas melhores, então... 
        Se ver minha esposa em algum lugar, diga que a amo."
        ''',
        ['Voltar'],
    ],
}
#Use este pedaço para atualizar o mapa.txt, caso faça alterações.
#with open('Mapa.txt','w') as Mapa_Txt:
#    Mapa_Json=json.dumps(Mapa,ensure_ascii=False,indent=4)
#    Mapa_Txt.write(Mapa_Json) 
    