#Read a file

f = open('file.txt', "r"); #By default the mode is r
data = f.read();

newList = data.split();

if ("This" in newList):
    print("This is present!!");


f.close();