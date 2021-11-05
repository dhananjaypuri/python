fname = "Dhananjay ";
lname = "Puri";

#Concatinating Strings
print("My name is : ", fname + lname);

#Print length of the string
print(len(fname));

#Slicing the strings  ==> Index start from 0 to (length-1)
print(fname[0:4]);
print(lname[:len(lname)]);
print(lname[-3:]);

newname = "amazing";
print(newname[1:len(newname):3]);
print(newname.endswith("ing") , " +++ ", newname.count('a'));