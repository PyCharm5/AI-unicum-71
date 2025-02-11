from math import *


def count_garlands(red, blue, yellow):
    return factorial(red + blue + yellow) // (factorial(red) * factorial(blue) * factorial(yellow))
print(count_garlands(4, 4, 8))


def count_teams(bandits, police, detective, passersby):
    return factorial(bandits + police + detective + passersby) // (factorial(bandits) * factorial(police) * factorial(detective) * factorial(passersby))
print(count_teams(2, 2, 1, 5))


def count_beads(green, blue, red):
    return factorial(green + blue + red) // (factorial(green) * factorial(blue) * factorial(red))
print(count_beads(4, 5, 6))


def count_fruits(apples, pears, oranges):
    return factorial(apples + pears + oranges) // (factorial(apples) * factorial(pears) * factorial(oranges))
print(count_fruits(2, 3, 4))


def count_bracelets(emeralds, rubies, sapphires):
    return factorial(emeralds + rubies + sapphires) // (factorial(emeralds) * factorial(rubies) * factorial(sapphires))
print(count_bracelets(5, 6, 7))