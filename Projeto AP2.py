"""Algoritmos e Programação de Computadores
 Projeto  AP2
Nomes: Leon Goldner - 1531717520219
       Leonardo Alfradique Diniz - 1911533963
       Luis Vitor - 1721533883
       Ana Carolina Ramos - 1531717110034
"""

def exercicio_117(nome_arq = 'lista_de_palavras.txt'):
    """Cria um jogo da forca com uma palavra escolhida aleatoriamente de
um arquivo de texto (.txt). Opcionalmente, o usuário pode colocar seu próprio
arquivo-fonte de palavras (uma espécie de dicionário sem definições)."""
    #Primeiro, precisamos abrir o arquivo-fonte de palavras e armazenar
    #a palavra correspondente à linha escolhida numa variável, em seguida
    #fechando o arquivo.
    import random
    linha_escolhida = random.randint(1,29858)
    arq = open(nome_arq)
    linha = 1
    while linha < linha_escolhida:
        arq.readline()
        linha += 1
    palavra = arq.readline().upper()
    arq.close()
    #Agora, escolhida a palavra, vamos montar o jogo propriamente dito.
    #REPL - READ-EVAL-PRINT-LOOP
    palavra_escondida = '_' * len(palavra)
    palavra_escondida_lista = list(palavra_escondida)
    palavra_lista = list(palavra)
    numero_de_erros = 0
    letra_encontrada = 0
    while True:
        letra = input("Digite uma letra: ").upper()
        primeira_pos = palavra.find(letra)
        if primeira_pos == -1:
            numero_de_erros += 1
            print(f"Você errou pela {numero_de_erros}ª vez. Tente de novo!")
        else:
            #Vamos considerar a princípio apenas palavras com 1 exemplar de cada letra
            #(o que restringe muito nosso espaço de palavras, mas tudo bem)
            palavra_escondida_lista[primeira_pos] = letra
            palavra_escondida = "".join(palavra_escondida_lista)
            print(f"A palavra é: {palavra_escondida}")
        #if letra in palavra:
            #primeira_pos = palavra.find(letra)
            #print("Parabéns! Você acertou.")
        #else:
            #print(f"Você errou pela {numero_de_erros}ª vez. Tente de novo!")
        if palavra_escondida == palavra:
            print(f"Parabéns! Você ganhou\nA palavra era: {palavra}")
            break
        if numero_de_erros == 6:
            print(f"Você perdeu! A palavra era: {palavra}")
