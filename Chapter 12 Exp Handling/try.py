# a = int(input("Enter the value of a : "));
# b = int(input("Enter the value of b : "));

while(True):

    a = input("Enter the value of a : ");
    b = input("Enter the value of b : ");

    if(a=='q' or b=='q'):
        break;
    
    try:
        sum = int(a) + int(b);
        print(f"The sum of the number is {sum}");
    except Exception as e:
        print(e);