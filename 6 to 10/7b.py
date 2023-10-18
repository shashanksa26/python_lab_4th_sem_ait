class Employee:
    employees = {}
    def __init__(self, name, id, dept, salary):
        self.name = name
        self.id = id
        self.dept = dept
        self.salary = salary
        Employee.employees[id] = self
    def update_salary(dept, increment):
        for id, employee in Employee.employees.items():
            if employee.dept == dept:
                employee.salary = employee.salary + increment
    def display():
        for id, employee in Employee.employees.items():
            print(employee.name, employee.id, employee.salary)
emp = Employee("A", 1, "CS", 100.0)
emp = Employee("B", 2, "IS", 200.0)
emp = Employee("C", 3, "CS", 300.0)
Employee.update_salary("CS", 50)
Employee.display()