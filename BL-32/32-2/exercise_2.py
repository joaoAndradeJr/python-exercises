"""
Jogo da palavra embaralhada. Desenvolva um jogo em que a pessoa usuária tenha
que adivinhar uma palavra que será mostrada com as letras embaralhadas. O
programa terá uma lista de palavras e escolherá uma aleatoriamente. O jogador
terá três tentativas para adivinhar a palavra. Ao final a palavra deve ser
mostrada na tela, informando se a pessoa ganhou ou perdeu o jogo. Para
embaralhar uma palavra faça:
scrambled_word = "".join(random.sample(word, len(word)))
O sorteio de uma palavra aleatória pode ser feito utilizando o método choice:
random.choice(["word1", "word2", "word3"]) -> "word2" .
"""

import random

words_list = [
    "azul",
    "revendedor",
    "seis",
    "angra",
    "pobreza",
    "biblioteca",
    "pulsar",
    "investimento",
    "tonelada",
    "fritar",
    "pilha",
]

random_word = random.choice(words_list)

scrambled_word = "".join(random.sample(random_word, len(random_word)))

print("A palavra é: " + scrambled_word)

counter = 0
win = False

while counter < 3 and win != True:
    guess = input("Digite a palavra correta: ")
    if guess == random_word:
        win = True
        print("Você Acertou!!!")
    if win == False:
        print("Você errou...")
    counter += 1
    if (counter == 3):
        print("Jogo encerrado!")
        print("A palavra era: " + random_word)
