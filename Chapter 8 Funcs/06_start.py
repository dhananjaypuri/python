#Print start

def star(n):
    for item in range(n):
        
        print("*" * (item+1));

def rev(n):
    for item in range(n):
        print("*" * (n-item));


num = 2;
star(num);
rev(num);