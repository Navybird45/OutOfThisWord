import random

import os

WORDS = (
    "treehouse",
    "python",
    "learner",
)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def prompt_for_words(challenge):
    guesses = set()
    print("What words can you find in the word '{}'".format(challenge))
    print("(Enter Q to QUIT)");
    while True:
        guess = input("{} words >  ".format(len(guesses)))
        if guess.upper() == 'Q':
            break
        guesses.add(guess.lower())
    return guesses

def output_results(results):
    for word in results:
        print("* " + word)

challenge_word = random.choice(WORDS)
player1_name = input("Player 1: ")
player2_name = input("Player 2: ")

clear_screen()

player1_words = prompt_for_words(challenge_word)

clear_screen()

player2_words = prompt_for_words(challenge_word)

print("{} Results:".format(player1_name))
player1_unique = player1_words - player2_words
print("{} guesses, {} unique".format(len(player1_words), len(player1_unique)))
output_results(player1_unique)
print("-" * 10)
print("{} Results:".format(player2_name))
player2_unique = player2_words - player1_words
print("{} guesses, {} unique".format(len(player2_words), len(player2_unique)))
output_results(player2_unique)

print("Shared guesses:")
shared_words = player1_words & player2_words
output_results(shared_words)
