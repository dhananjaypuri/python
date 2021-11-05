#Convert from Celcius to faren


def convert(a):
    result = (a*9/5)+32;
    return result;

num = float(input("Enter the temperature in Degree : "));

print(convert(num));