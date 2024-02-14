import csv

region_to_search = input()

winners_in_region = []

with open('olymp.csv', mode = 'r', encoding = 'utf-8') as file:
	csv_reader = csv.reader(file)

	for line in csv_reader:
		name, region, points, status = line
		if region.strip() == region_to_search.strip() and status.strip() == "Winner":
			winners_in_region.append(', '.join(line))

for line in winners_in_region:
	print(line)
