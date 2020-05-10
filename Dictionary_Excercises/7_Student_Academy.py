student_dict = {}
number_of_students = int(input())
for i in range(number_of_students):
    student = input()
    grade = float(input())
    if student not in student_dict:
        student_dict[student] = [grade]
    else:
        student_dict[student] += [grade]
top_students = {student_name: sum(student_grade) / len(student_grade) for student_name, student_grade in
                student_dict.items() if
                sum(student_grade) / len(student_grade) >= 4.5}
top_students = {k: v for k, v in sorted(top_students.items(), key=lambda item: item[1], reverse=True)}
for i, v in top_students.items():
    print(f"{i} -> {v:.2f}")
