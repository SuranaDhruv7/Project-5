print("--- Python OOP Project: Employee Management System ---\n")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def get_employee_id(self):
        return self.employee_id
    
    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_employee_salary(self):
        return self.salary
    
    def set_employee_id(self, salary):
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Salary: ${self.salary: .2f}")

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department = None):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programing_language):
        super().__init__(name, age, employee_id, salary)
        self.programing_language = programing_language

    def display(self):
        super().display()
        print(f"Programing Language: {self.programing_language}")

person = []
employees = {}
manager = {}    
is_on = True
while is_on:
    choice = int(input("Choose an operation:\n1. Create a Person\n2. Create an Employee\n3. Create a Manager\n4. Show Details\n5. Compare Salaries\n6. Exit\nEnter your choice: "))
    if choice == 1:
        new_name = input("Enter Name: ")
        new_age = int(input("Enter Age: "))
        p = Person(new_name, new_age)
        person.append(p)
        print(f"Person created with name: {new_name} and age: {new_age}")
        print("\n--- Choose another operation ---\n")
    
    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        e = Employee(name, age, emp_id, salary)
        employees[emp_id] = e
        print(f"Name: {name}, Age: {age}, Employee ID: {emp_id}, Salary: ${salary}")
        print("\n--- Choose another option ---\n")
    
    elif choice == 3:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter department: ")
        m = Manager(name, age, emp_id, salary, department)
        manager[emp_id] = m
        print(f"Manager created with Name: {name}, Age: {age}, Employee ID: {emp_id}, Salary: ${salary}, Department: {department}")
        print("\n--- Choose another option ---\n")
    
    elif choice == 4:
        print("Choose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(f"\n--- Person details ---\n")
            for p in person:
                print(p)
        
        elif choice == 2:
            print(f"\n--- Employee details ---\n")
            for emp in employees.values():
                emp.display()

        elif choice == 3:
            print("\n--- Manager details ---\n")
            for m in manager.values():
                m.display()
        
        else:
            print("INVALID CHOICE..")
    
    elif choice == 5:
        print("\nChoose two employees to compare salaries: ")
        id1 = input("Enter the first employees's ID: ")
        id2 = input("Enter the second employees's ID: ")
        if id1 in employees and id2 in employees:
            e1 = employees[id1]
            e2 = employees[id2]
            print("\nComparing Salaries...")
            if e1 > e2:
                print("f{e1.name} ({id1}) has higher salary than {e2.name} ({id2}).")
                
            elif e1 < e2:
                print("f{e1.name} ({id1} has lower salary than {e2.name} ({id2}).")

            else:
                print("f{e1.name} ({id1}) and {e2.name} ({id2}) have equal salaries.")

        else:
            print("INVALID CHOICE!")   
    elif choice == 6:
        print("\nExiting the system. All resources have been feed.\n")
        is_on = False
    else:
        print("\nINVALID CHOICE!\n")
        is_on = False