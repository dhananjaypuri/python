#Format is a replacement for f strings

fname = "Dhananjay";
lname = "Puri";

try:
    strr = "My name is {} {}.".format(fname,lname);
    print(strr);
    strr = "My Lastname is {1} and my first name is {0} .".format(fname,lname);
    print(strr);
except IndexError as e:
    print(e);
else:
    print("This means Try block succeded !!!!! ");
finally:
    print("This Block will execute at any cost !!!!! ");