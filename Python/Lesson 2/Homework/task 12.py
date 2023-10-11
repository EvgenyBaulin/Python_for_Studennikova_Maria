strin = input().split(', ')

citis = {}

sum = 0
n = len(strin)

for i in strin:
	i = i.split(':')

	if '+' in i[1]:
		i[1].replace('+', '')

	sum += int(i[1])
	citis[i[0]] = int(i[1])

aver = sum / n

result = {}

for city, temp in citis.items():
	if temp >= aver:
		result[city] = temp

result = {k: v for k, v in sorted(result.items(), key = lambda item: item[1], reverse = True)}

print(result)
