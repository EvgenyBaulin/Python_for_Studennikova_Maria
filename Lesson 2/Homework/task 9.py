grades = {"John": 3.7, "Alex": 3.9, "Sarah": 3.4, "Emily": 4.0, "Michael": 3.5,
		  "Jessica": 3.8, "Daniel": 3.6, "Olivia": 4.1, "William": 3.2,
		  "Sophia": 4.2, "David": 3.3, "Emma": 2.9, "Andrew": 3.1, "Grace": 4.3,
		  "Ethan": 3.0}

sorted_students = sorted(grades.keys(), key = lambda x: grades[x], reverse = True)

rating = int(input())

student_name = sorted_students[rating - 1]
print(student_name)
