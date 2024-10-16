from altcolor import *

# Colored text allows you to paint your words with RGB
print(colored_text((244, 5, 7), "Hello World!"))

# Here's a regular print
print("Hello World!")

# We even have predefined colors
print(colored_text("BLUE", "Hello World!"))


# Leaked text splills into other print statements until you use reset()
print(leaked_text("RED", "Hey,"))
print("you")
print("are" + reset())

# Leaked text can even spill into the background
print(leaked_text("WHITE", "cool!", "Back"))
print("How")
print("are")
print("you?" + reset())