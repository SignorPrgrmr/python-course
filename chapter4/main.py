name = 'AminAA'

# len
print(len(name))
print(len("Amin Farzane"))

# index
print(name.index('Am'))

# count
print(name.count("A"))

# Accessing characters
print(name[0])
print(name[1:4])

# upper & lower
print(name.upper())
print(name.lower())

# split
full_name = 'Amin Farzane Ghazani'
# Amin Farzane Ghazani
ayrilmish = full_name.split(' ')
print(ayrilmish)

print("---------------------------------")

# Replace
name = name.replace('AA', ' Farzane')
print(name)
