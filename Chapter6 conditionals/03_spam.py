#Check if spam is there

text = input("Enter the Text : ");

if("make a lot of money" in text):
    spam = True;
elif("buy now" in text):
    spam = True;
elif("click this" in text):
    spam = True;
elif("subscribe this" in text):
    spam = True;
else:
    spam = False;

if(spam==True):
    print("This is Spam!!!!");
else:
    print("You are good to go");