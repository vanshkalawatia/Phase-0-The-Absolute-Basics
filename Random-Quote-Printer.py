"""
Project: Random Quote Printer

what it needs: print(), lists, random.choice()

what it is: A script that prints a random quote from a hardcoded list.
"""

import random as rn

russian_quotes = [
    "If you want to be happy, be. — Leo Tolstoy",
    "The two most powerful warriors are patience and time. — Leo Tolstoy",
    "The sole meaning of life is to serve humanity. — Leo Tolstoy",
    "If you want to work on your art, work on your life. — Anton Chekhov",
    "The mystery of human existence lies not in just staying alive, but in finding something to live for. — Fyodor Dostoevsky",
    "When work is a pleasure, life is a joy! When work is a duty, life is slavery. — Maxim Gorky",
    "Man is born to live, not to prepare for life. — Boris Pasternak",
    "It is no use to blame the mirror if your face is skewed. — Nikolai Gogol",
    "If we wait for the moment when everything, absolutely everything, is ready, we shall never begin. — Ivan Turgenev",
    "Better the illusions that exalt us than ten thousand truths. — Alexander Pushkin"
]


print(rn.choice(russian_quotes))
