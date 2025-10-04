# Ask user for their name
name = input("What's your name? ").strip().title()

# Strip function removes whitespace before and after a string
#name = name.strip()

# Capitalize the user's name, but only the first letter
#name = name.capitalize()

# Capitalize the user's whole name
#name = name.title()

#name = name.strip().title()

# Say hello to user
#print("Hello,", name)

# Split user's name into first name and last name
first, last = name.split()

# Let's do it with an f string instead
print(f"Hello, Mr. {last}")