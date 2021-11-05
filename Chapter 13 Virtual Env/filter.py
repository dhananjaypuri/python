l = [1,2.5,4,5,10,100,40,89,77];

def greater_than_5(num):
    if num > 5:
        return True;
    else:
        return False;

greater_than_10 = lambda num: num>10;

print(list(filter(greater_than_5,l))); #This will print a list of number greater than 5

print(list(filter(greater_than_10,l))); #This will print a list of number greater than 10