from termcolor import cprint

colors = ["red", "green", "blue", "magenta", "yellow"]

# Tell the user the instructions
print(f"Hello user! What color would you like 'Hello world' to be printed with?\nChoose among: {', '.join(colors)}")

# Take the input from the user
color = input("-->")

# Check if the input is in the available colors: if not, tell the user that it is not available
if color.lower() in colors:
    cprint("Hello world!", color=color)
else:
    print("ERROR! The color you chose is not among the available colors :(")   
