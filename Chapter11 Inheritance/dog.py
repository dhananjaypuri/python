class Animal:

    animalType = "Mammal";

class Pet(Animal):

    petType = "Dog";

class Dog(Pet):

    dogName = "Americal Bully";

    def display(self, dname):
        self.dogName = dname

        print(f'''\t\t  Animal Type :{self.animalType}
                  Pet Type : {self.petType}
                  Dog Name : {self.dogName}''');

dg = Dog();

dg.display("Bully");