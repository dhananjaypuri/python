#Print sum of n number

def sumofn(num1):
    i = 1;
    sum = 0;
    while(i<=num1):
        sum = sumofn(num1-1) + i;
        i +=1;
    return sum;

num = int(input("Enter the Number : "));
result = sumofn(num);
print(result);