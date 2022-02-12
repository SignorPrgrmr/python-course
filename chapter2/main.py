# Basic communicating through I/O (In Terminal)

print("Amin")
# not "amin"

print('------------------------------------')

# Variables

name = 'Amin'
print(name)

print('------------------------------------')
# Data Type

# Number

# Integer
age = 20

# Float
weight = 50.3

# Operators of numbers
summing = 20 + 50
multiply = 50 * 60
division = 10 / 3
minus = 30 - 10
power = 2 ** 3
division2 = 10 // 3
remaining = 10 % 3

result = 5 * 2 + 3 ** 2

print(summing, multiply, division, minus, power, division2, remaining)

print('-----------------------------------------')
# String

name = "Amin"
# Strings should be inside of '' or ""

# Operator
firstname = "Amin"
lastname = "Farzane"

fullname = firstname + ' ' + lastname + ' '

three_times_fullname = fullname * 3
print(firstname + ' F' * 3)
print('------------------------------')
# Boolean
isComplete = False

# Operators

isGone = True and (False or False)

# AND
# true and true -> true
# true and false -> false
# false and true -> false
# false and false -> false

# OR
# true or true -> true
# true or false -> true
# false or true -> true
# false or false -> false

print(isGone)

print('--------------------------------')

# Lists
scores = [2, 5, 8, 6, 3, 9, 124, 14, 125]

# Appending
scores.append(20)

print(scores)

# Accessing the elements of a list.

print('--------------------------------------')

print(scores[6])
print('Size of scores: ', len(scores))

# List Operators

print('--------------------------------------')

first_list = [1, 2, 3, 4]
second_list = [5, 6, 7, 8]

result_list = first_list + second_list  # [1, 2, 3, 4, 5, 6, 7, 8]

another_list = 3 * first_list + second_list

print(result_list)
print('Counting 1: ', another_list.count(1))

