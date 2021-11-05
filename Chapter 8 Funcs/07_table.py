
#Prints table

def table(n):
    for item in range(1,11):
        print(f"{n} * {item} = ", (n*(item)));
        
num = int(input("Enter the number : "));        
table(num);        