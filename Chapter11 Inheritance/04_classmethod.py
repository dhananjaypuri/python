class Employee:

    salary = 1000;
    country = "India";

    # @classmethod
    # def changesal(cls, sal): #This will change the value of 
    #     cls.salary = sal;

class Programmer(Employee):
    
    def display(self, name):
        self.name = name;
        print(f'''\t\t  Name: {self.name}
                  Salary: {self.salary}''');
    @classmethod
    def changesal(cls, sal2): #This will change the value of 
        cls.salary = sal2 + 2;                  
    @staticmethod
    def new(lang):
        print(f"{lang}");
pr = Programmer();

pr.display("Neeraj");
pr.changesal(40000);
pr.display("Neeraj");
pr.new("English");