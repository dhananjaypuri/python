try:
    a = int(input("Enter the value of a : "));
    c = 1/a;

    print("The answer is : ", c);
except ZeroDivisionError as e:
    print("You cannot devide a number by 0 !!");
except TypeError as e:
    print(e);
except ValueError as e:
    print("This is value error : ", e);
except KeyboardInterrupt as e:
    print("Keyboard : ", e);

# print(__name__);