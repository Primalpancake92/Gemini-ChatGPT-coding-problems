class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age 
        self.grade = []
        
    
    def add_grade(self, grade: float): 
        self.grade.append(grade)
        
    
    def average_grade(self):
        total = sum(value for value in self.grade)
        return total / len(self.grade)
    
    
    def get_student_info(self):
        return f"Student name: {self.name}\nAge: {self.age}\nGrades: {self.grade}"
    

if __name__ == "__main__":
    student = Student("John", 20)
    student.add_grade(85.5)
    student.add_grade(90.0)
    student.add_grade(88.0)

    print(student.average_grade())  # Should print the average of the grades (87.83)
    print(student.get_student_info())  # Should print student details
