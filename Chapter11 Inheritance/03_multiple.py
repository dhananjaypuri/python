class Person:               ##Base Class
    country = "India";

class Employee:   #Base Class
    company = "Youtube";
    ecode = 1111;

class Programmer(Person , Employee):  ##Derived Class From Person and Employee

    def __init__(self, name , ecode):
        self.name = name;
        self.ecode = ecode;
        
    def display(self):
        print(f'''\t\t  Name: {self.name}
                  Ecode: {self.ecode}
                  Company: {self.company}
                  Country: {self.country}''');

pr = Programmer("Dhananjay Puri", 1122);
# pr.company = "Samsung";
pr.display();