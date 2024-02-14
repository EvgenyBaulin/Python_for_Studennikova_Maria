# name = input()
# age = int(input())
#
# print(f'The person named {name} will be {age + 1} years old in one year!')


# ok = 'Match'
# not_ok = 'Something is wrong'
#
# a = input()
# b = input()
#
# if len(a) > 5 and a.startswith(b):
# 	print(ok)
# else:
# 	print(not_ok)

# a = input()
# b = []
#
# while a != '0':
# 	if len(a) < 7 and a.isalpha():
# 		b.append(a)
#
# 	a = input()
#
# print(b)

# b = []
#
# while True:
# 	a = input()
# 	if a == '0':
# 		break
# 	if len(a) < 7 and a.isalpha():
# 		b.append(a)
#
# print(b)

# words = input().split()
# answer = []
#
# for word in words:
# 	for char in word:
# 		if char.isupper():
# 			answer.append(word.lower())
# 			break
#
# answer.sort()
#
# print(answer)

# animals_Katya = input().split()
# animals_Petya = input().split()
# animals_allergic = input().split()

# animals_Katya = 'foxy tiger fish lion kitty pug mouse'.split()
# animals_Petya = 'tiger bunny lion fish foxy kitty mouse'.split()
# animals_allergic = 'tiger'.split()
#
# answer = sorted(set(animals_Katya) & set(animals_Petya) - set(animals_allergic))
#
# answer = ', '.join(answer)
# print(answer)

# d = {'Maria': {'Age': 18, 'City': 'Moscow'}, 'Evgeny': {'Age': 18, 'City': 'Moscow'}}
#
# print(d['Maria']['City'])
