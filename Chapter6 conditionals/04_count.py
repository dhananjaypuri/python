#Count is name is less than 10 characters.

text = input("Please enter the name : ");

length = int(len(text));

if(length<10):
    print("Not Allowed !!!! Name is less than 10 Characters!!!!!");
else:
    print("You are good to go!!!!");
