# Store firstname and lastname in a variable and print your fullname.

# firstname = 'zahra'
# lastname = 'salahpour'
# print(firstname, lastname)

# Pi = 3.14, radius = r, print
# r = 2
# pi = 3.14
# area = pi * r ** 2
# print(area)

# prepend 0 at the beginning of a list using +
# list = [1, 2, 3]
#
# result = [0] + list
#
# print(result)

# Home Exercise
# 1. magadire 3 va 5 ra be tartib daxele a va b garar dahid va jabeja konid (hint: ba estefade az c)
# 2. magadire 3 va 5 ra be tartib daxele a va b garar dahid va bedune hafezeye ezafi jabeja konid
# 3. magadire 3 va 5 va 7 ra be tartib daxele a va b va c garar dahid va jabeja konid
# 4. magadire 3 va 5 va 7 ra be tartib daxele a va b va c garar dahid va bedune estefade az hafezeye ezafi jabeja konid.

# 1.
# a, b = 3, 5
# c = a
# a = b
# b = c

# 2.
# a, b = 3, 5
# a = a + b
# b = a - b
# a = a - b
# a, b = 3, 5
# a, b = b, a

# 3.
# a, b, c = 3, 5, 7
# d = a
# a = b
# b = c
# c = d

# 4.
# a, b, c = 3, 5, 7
# a, b, c = b, c, a


# Home Exercise
# 1. Yek list'e xali tarif karde va be tartib nam, nam'e xanevadegi & senne xod ra be list append konid
# 2. daxele haman list dar andise 2 pasvande familiye xod ra ezafe konid
# 3. xanei ke nam ra dar an qarar dadeid ba sen jabeja konid +
# 4. yek payam ba estefade az magadire list chap konid ke be shekle zir bashad
#   'My name is Amin Farzane Ghazani. I'm 20 years old'
# [20, 'Farzane', 'Ghazani', 'Amin']

# # 1
# my_list = []
# my_list.append('Amin')
# my_list.append('Farzane')
# my_list.append(20)
#
# # 2
# my_list.insert(2, 'Ghazani')
#
# # 3
# my_list[0], my_list[3] = my_list[3], my_list[0]
#
# # 4
# print("My name is %s %s %s. I'm %d years old" % (my_list[3], my_list[1], my_list[2], my_list[0]))

# 1. ba estefade az function input() yek jomle az karbar daryaft konid va on ra daxele motaghayyeri zaxire konid
# 2. character'e 'H' va 'h' ra be name xod tabdil konid va chap konid
# 3. tule reshteye jadid ra chap konid
# 4. jomle ra ta nesfe xodash chap konid +
# 5. kalamate jomle ra jodagane chap konid +

# 1
sentence = input('Please enter something: ')

# 2
changed_sentence = sentence.replace('H', 'Amin').replace('h', 'Amin')

# 3
print('Length of new sentence: ', len(changed_sentence))

# 4
length_of_sentence = len(sentence)
half_of_length = length_of_sentence // 2
print(sentence[0:half_of_length + 1])

# 5
words = sentence.split(' ')
print(words)

