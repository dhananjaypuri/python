#Find greater of 4 numbers

num1 = int(input("Enter the value of number 1 : "));
num2 = int(input("Enter the value of number 2 : "));
num3 = int(input("Enter the value of number 3 : "));
num4 = int(input("Enter the value of number 4 : "));

if(num1>num4):
    greater1 = num1;
elif(num4>num1):
    greater1 = num4;

if(num2>num3):
    greater2 = num2;
elif(num3>num2):
    greater2 = num3;

if(greater1>greater2):
    print("The greatest number is :" , greater1);
else:
    print("The greatest number is :" , greater2);