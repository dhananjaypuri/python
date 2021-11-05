class Calculator:
    
    def __init__(self, num):
        self.number = num;
        print(f"The entered number is {self.number}");

    def square(self):

        sq = (self.number **2);
        print(f"The square of {self.number} is {sq}");

    def cube(self):

        cube = (self.number **3);
        print(f"The Cube of {self.number} is {cube}");   
    
    def squareRoot(self):

        sqr = (self.number **0.5);
        print(f"The Square Root of {self.number} is {sqr}");

    @staticmethod  #This is a static method it does not require Self argument
    def greet():
        print("Hello User ,");

number1 = int(input("Enter the number : "));

calc = Calculator(number1);

calc.greet();
calc.square();
calc.squareRoot();
calc.cube();