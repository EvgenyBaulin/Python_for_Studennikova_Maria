airlines = {
	'Airline_1': {
		'Plane_1': ['City_A', 'City_B', 'City_C'],
		'Plane_2': ['City_B', 'City_D'],
	},
	'Airline_2': {
		'Plane_3': ['City_A', 'City_C'],
		'Plane_4': ['City_D'],
	},
}

city_to_check = input()

planes_count = 0

for airline, planes in airlines.items():
	for plane, cities in planes.items():
		if city_to_check in cities:
			planes_count += 1

print(planes_count)
