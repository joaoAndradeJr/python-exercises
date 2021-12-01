# Modifique o exercício anterior para que as palavras sejam lidas
# de um arquivo. Considere que o arquivo terá cada palavra em uma linha

import random

words_list = open("words_list.txt", mode="r")
words = words_list.read().split('\n')

random_word = random.choice(words)

scrambled_word = "".join(random.sample(random_word, len(random_word)))

print("A palavra é: " + scrambled_word)

counter = 0
win = False

while (counter < 3 and win != True):
    guess = input("Digite a palavra correta: ")
    if (guess == random_word):
        win = True
        print("Você Acertou!!!")
    if (win == False):
        print("Você errou...")
    counter += 1
    if (counter == 3):
        print("Jogo encerrado!")
        print("A palavra era: " + random_word)
