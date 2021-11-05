#Append a file

data = "\nData Appended!!!!";

f = open("newfile.txt", "a");
f.write(data);
f.close();