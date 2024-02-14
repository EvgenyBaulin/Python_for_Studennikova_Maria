grades_input = input()
grades_dict = dict(item.strip().split(': ') for item in grades_input.split(', '))

satisfactory_grade = int(input())

subjects_to_improve = []

for subject, grade in grades_dict.items():
	if int(grade) < satisfactory_grade:
		subjects_to_improve.append(subject)

subjects_to_improve.sort()

if subjects_to_improve:
	print(", ".join(subjects_to_improve))
else:
	print()
