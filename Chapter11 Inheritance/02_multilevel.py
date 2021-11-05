class Person:               ##Base Class
    country = "India";

    def displaysal(self):
        print(self.country);

class Employee(Person):     ##Derived Class
    salary = 100;
    company = "Samsung";

    def displaysal(self, name):
        self.name = name;
        print(f"The name of user is : {self.name} and the company is {self.company} and salary is {self.salary} and the country is {self.country}");

class Programmer(Employee):  ##Derived Class
    def __init__(self, lang, empcode, name):
        self.lang = lang;
        self.empcode = empcode;
        self.name = name;

    def displaysal(self, sal):
        self.salary = sal;
        super().displaysal(self.name);      ##This is super method , this is execute the method of latest derived class
        print(f'''\t\t  Name : {self.name}
                  Country: {self.country}
                  Company: {self.company}
                  Language: {self.lang}
                  Salary: {self.salary}''');


pr = Programmer("Python",1111,"Harsh Sharma");      

pr.displaysal(45000);