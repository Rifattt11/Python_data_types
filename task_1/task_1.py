students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]},
    {"name": "Bob", "grades": [4, 4, 4, 5]},
    {"name": "Charlie", "grades": [5, 5, 5, 5]},
]

students_average_marks = {}

for student in students:
    average_mark = sum(student['grades']) / len(student['grades'])
    students_average_marks[student['name']] = average_mark

best_student = max(students_average_marks, key=students_average_marks.get)

print(students_average_marks)
print(best_student, students_average_marks[best_student])