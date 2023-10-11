money = int(input())

products = {"Mobile Phone": 500, "Laptop": 1200, "Television": 800, "Headhones": 150, "Tablet": 350}

result = {}

products = {k: v for k, v in sorted(products.items(), key = lambda item: item[1], reverse = True)}

for item, cost in products.items():
	if money - cost >= 0:
		money -= cost
		result[item] = cost

result_2 = []

for item, cost in result.items():
	result_2.append(item)

result_2 = ', '.join(result_2)

print(result_2)
