# (a+bi) + (c+di) = (a+c) + (b+d)i   #Dunder Methods this explains operator overloading

class Complex:

    def __init__(self, a, b):
        self.real = a;
        self.img = b;

        #print(f"Real : {self.real}, Imaginary: {self.img}");
    
    def __add__(self, other):
        return(f"{self.real + other.real} + {self.img + other.img}i");

c1 = Complex(1,2);
c2 = Complex(3,14);

c3 = c1 + c2;

print(c3);