# == < > <= >= !=

# if condition:
#   statement
# elif another_condition:
#   another_statement
# else:
#   else_statement

if 4 > 10:
    print("If block is running")
elif 4 > 8:
    print('Elif block is running')
else:
    print("Else block is running")

lst = ["Amin", "Farzane", "Ghazani", 20]

if 'Amin' in lst:
    print('There is Amin in list')
else:
    print('There is not Amin in list')

print('-----------------------------------')

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]

lst1.append(4)

print(lst2)

if lst1 == lst2:
    print("Name is equal with first_name")

if lst1 is lst2:
    print("Name is first_name")

print('----------------------------------')

is_equal = not 4 == 5

print(is_equal)