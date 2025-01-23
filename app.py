from termcolor import cprint
import random
# random is the library that allows us to extract random items from a list
colors = ["red", "green", "blue", "magenta", "yellow"]

color = random.choice(colors)

cprint("Hello world!", color=color)
