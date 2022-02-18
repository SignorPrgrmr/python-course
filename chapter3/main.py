# List Data Type
my_list = [1, 2, 3, 4, 5, 6, 7]

# Dastrasi be xanehaye list
my_variable = my_list[0]
my_variable = my_list[6]

# Append
my_list.append(56)

# Inserting in every position
my_list.insert(1, 8)

# Operator

# Concatenation
my_list = my_list + [9, 10, 12]

# Multiply
my_list = my_list * 3

print(my_list)

# String formatting
name = 'Amin'
age = '20'
math_score = 20 / 3 * 2

message = "Your name is %s and you're %s years old. Your score in math is %.10f" % (name, age, math_score)

print('A message has arrived: %s' % message)
print(math_score)
