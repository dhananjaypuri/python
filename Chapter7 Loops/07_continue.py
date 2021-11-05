#Continue statement ==> This is opposite of break

newList = ["Apple", "Mango", "Banana", "Guava"];

for item in newList:
    if(item=="Banana"):
        continue;   #This will skip this part once item == Banana
    else:
        print(item);