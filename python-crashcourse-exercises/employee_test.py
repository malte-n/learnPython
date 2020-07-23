class Employee:
    def __init__(self, first_name, last_name, annual_salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, employee_raise=0):
        if employee_raise == 0:
            self.annual_salary += 5000
        else:
            self.annual_salary += employee_raise
