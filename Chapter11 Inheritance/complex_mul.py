                        # (ac−bd) + (ad+bc)i this is the formulae for Complex number multiplication
class Complex:

    def __init__(self, i , j):
        
        self.icap = i;
        self.jcap = j;
        
    def __mul__(self, other):

        mulReal = (self.icap * other.icap)-(self.jcap * other.jcap);
        mulImg = (self.icap * other.jcap)+(self.jcap * other.icap);
        print(f"({mulReal})+({mulImg})i");


comp1 = Complex(3,2);
comp2 = Complex(1,7);

print(comp1 * comp2);