#!/usr/bin/python3
"""This program should print a story based on user input,
a Mad libs game as a python program.
"""
print("""Welcome to my Mad libs!

      You'll be asked for a set of words (e.g. adjectives, noun, ...)
      and you should provide them based on the number specified and
      they must be ', ' seperated (Apple, Horse, gold). if you wanna use
      a word multiple times you should repeat it; e.g nouns: cat, cat.

      ENJOY!
""")

adjectives_str: str = input("Type four adjectives:\n")
adjectives = adjectives_str.split(", ")

nouns_str: str = input("Type three nouns:\n")
nouns = nouns_str.split(", ")

plural_nouns_str: str = input("Type three plural nouns:\n")
plural_nouns = plural_nouns_str.split(", ")

present_verbs_str: str = input("Type two present tense verbs (doing, do):\n")
present_verbs = present_verbs_str.split(", ")

past_verbs_str: str = input("Type two past tense verbs:\n")
past_verbs = past_verbs_str.split(", ")

adverbs_str: str = input("Type one Adverb\n")
exclame: str = input("Type one exlamation (e.g. Wow or Crazy):\n")

print("\n" * 2, "A trip to the Zoo")
print(f"\tYesterday, I went to the zoo.", end="")
print(f" I saw some {adjectives[0]:s} {plural_nouns[0]:s}.")
print(f"\tThey {past_verbs[0]:s} {adverbs_str:s}.")
print(f"\tOne {nouns[0]:s} was so {adjectives[1]:s} that ", end="")
print(f"the {plural_nouns[1]:s} started {present_verbs[0]:s}.")
print(f"\t{exclame:s}! The {plural_nouns[2]:s} were {adjectives[2]:s},")
print(f"\tand they liked to {present_verbs[1]:s} a {nouns[2]:s} ", end="")
print(f"on their {nouns[0]:s}.")
print(f"\tI saw a {adjectives[3]:s} {plural_nouns[0]:s}", end="")
print(f" that {past_verbs[1]:s} in the {nouns[1]:s}")
print("\t(END)\n")
