class Employee:
    
    salary = 1000;
    bonus = 500;

    @property
    def salaryAfterInc(self):
        return(f"The incremented salary is {float(self.salary) + float(self.bonus)}");

    @salaryAfterInc.setter
    def salaryAfterInc(self, salinc):
        self.bonus = salinc - self.salary;
        return (self.bonus)

emp = Employee();

print(emp.salaryAfterInc);

emp.salaryAfterInc = 7000;

print(emp.bonus);