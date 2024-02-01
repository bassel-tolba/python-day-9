student_socores = {"harry": 81, "ron" : 78, "hermione" : 99, "drako" : 74, "neville" : 62, }
student_grades = {}
for student in student_socores:
    if student_socores[student] >= 91 and student_socores[student] < 100:
        print(f"the student {student} is outstanding ")
        student_grades[student] = ["outsanding"]

    elif student_socores[student] >= 81 and student_socores[student] < 90:
        print(f"the student {student} exceeds expectations ")
        student_grades[student] = ["exceeds expectations"]

    elif student_socores[student] >= 71 and student_socores[student] < 80:
        print(f"the student {student} is acceptable ")
        student_grades[student] = ["acceptable"]

    elif student_socores[student] <= 70:
        print(f"the student {student} is a failor ")
        student_grades[student] = ["failor"]
print(student_grades)