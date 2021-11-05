def sum(a,b,c):
    return (a+b+c);

num1 = int(input("Enter the value of num1 : "));
num2 = int(input("Enter the value of num2 : "));
num3 = int(input("Enter the value of num3 : "));


lam_sum = lambda x,y,z: (x+y+z) #Syntax for creating sum function in lambda
lam_sqaure =  lambda sq: (sq*sq) #Syntax for creating sum function in lambda

print("The sum is : ",sum(num1,num2,num3));
print("The sum is (Lambda Function) : ",lam_sum(num1,num2,num3));
print("The square is (Lambda Function) : ",lam_sqaure(num1));