#Check if the entered name is present in the list or not!!!!!

name = input("Enter the name : ");

nameList = ["harry", "sherry", "arun", "varun"];

if(name in nameList):
    print("This is present in the list");
else:
    print("Name not in the list !!!!!");
    nameList.append(name);
    print(nameList);        