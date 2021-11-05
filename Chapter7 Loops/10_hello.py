#Print hello for the user whose name start with S

newList = ["Harry", "Sachin" , "Sapna", "Rini"];

for item in newList:
    if(item.startswith("S")):
        print(f"Hello {item},");
    else:
        continue;