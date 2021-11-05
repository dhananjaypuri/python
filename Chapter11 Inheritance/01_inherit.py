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

p = Person();
ee = Employee();
ee.displaysal("Dhananjay Puri");
