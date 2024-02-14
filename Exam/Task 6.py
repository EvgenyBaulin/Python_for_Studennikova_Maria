presidents = {
	'Non-Partisan': [('George Washington', 1789, 1797), ('John Tyler', 1841, 1845)],
	'Democrat-Republican': [('Thomas Jefferson', 1801, 1809), ('James Monroe', 1817, 1825)],
	'Democrat': [('Franklin Pierce', 1853, 1857), ('Grover Cleveland', 1893, 1897)],
	'Republican': [('William Taft', 1909, 1913)]
}

event_year = int(input())
party_affiliation = input()

president = False

for name, start_year, end_year in presidents[party_affiliation]:
	if start_year <= event_year <= end_year:
		president = name
		break

if president:
	print(president)
