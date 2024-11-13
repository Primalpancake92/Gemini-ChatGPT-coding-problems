def grades_dictionary(grades):
    max = 0
    top_student = ""
    for student, grade in grades.items():
        if grade > max:
            max = grade
            top_student = student
            
    return top_student, max


grades = {'Alice': 85, 'Bob': 92, 'Charlie': 88}
print(grades_dictionary(grades))