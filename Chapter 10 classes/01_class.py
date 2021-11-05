class Programer:
    company = "Microsoft";
    def __init__(self, name, product):
        print("Object is being created");
        self.name = name;
        self.product = product;
    def getinfo(self):
        print(f"The name of the user is {self.name} and the product he is using is {self.product}");

dhananjay = Programer("Dhananjay Puri", "Ms Office");
nishant = Programer("Nishant Sharma", "NodeJS");

dhananjay.getinfo();
nishant.getinfo();