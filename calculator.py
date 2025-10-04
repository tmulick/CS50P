x = float(input('What\'s x? '))
y = float(input('What\'s y? '))

z = x / y

# Use an f string to automatically add commas to large numbers
#print(f"{z:,}")

# Use an f string to round decimals to 2 places
print(f"{z:.2f}")