class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")


employee1 = Employee(name="John Doe", employee_id="E001", salary=50000)
employee2 = Employee(name="Alice Smith", employee_id="E002", salary=60000)
employee3 = Employee(name="Bob Johnson", employee_id="E003", salary=55000)


print("Employee 1 details:")
employee1.display_employee_details()
print("\nEmployee 2 details:")
employee2.display_employee_details()
print("\nEmployee 3 details:")
employee3.display_employee_details()
