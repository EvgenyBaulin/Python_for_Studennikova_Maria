num_students = int(input())

grades_dict = {}

for _ in range(num_students):
	strin = input().split()
	try:
		grades_dict[strin[0].lower()] = int(strin[1])
	except:
		grades_dict[strin[1].lower()] = int(strin[0])

student = input().lower()

flag = True

for k, v in grades_dict.items():
	if student == k:
		print(v)
		flag = False
		break

if flag:
	print('The student did not come to the exam')
