print("Lets Play who is greater!!!!");

num4 = int(input("Enter the value of Num4 : "));
num5 = int(input("Enter the value of Num5 : "));
num6 = int(input("Enter the value of Num6 : "));

great = False;

def greater(n1,n2,n3):
    if (n1>n2):
        g1 = n1;    
    else:
        g1 = n2;
    if (g1>n3):
        g2 = g1;
    else:
        g2 = n3;
    return (g2);



result = greater(num4,num5,num6);
print(result);