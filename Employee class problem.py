class Employee:
    def __init__(self, employee_ID: int, name: str, department: str, salary: float):
        self.employee_ID = employee_ID
        self.name = name
        self.department = department
        self.salary = salary
        
    
    def apply_raise(self, performance):
        if performance == "Excellent":
            return (0.10 * self.salary) + self.salary
        return (0.05 * self.salary) + self.salary

    
    def get_employee_info(self, performance):
        self.salary = self.apply_raise(performance)
        return f"\nEmployee ID: {self.employee_ID}\nName: {self.name}\nDepartment: {self.department}\nSalary: {self.salary}\n" 
    

def main():
    
    n = int(input())
    for i in range(n):
        employee_ID, name, department, salary, performance = input().split(" ")
        employee_details = Employee(int(employee_ID), name, department, float(salary))
        print(employee_details.get_employee_info(performance))
        

if __name__ == "__main__":
    main()