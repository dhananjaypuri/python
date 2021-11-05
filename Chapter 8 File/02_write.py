#Write into file

f = open("newfile.txt", "w");
data = "This is a new file . \n How are you !!!!!";
f.write(data);
f.close();