#Create a copy of a file

with open("donkey.txt", "r") as f:
    content = f.read();
    if(content==""):
        print("File is empty!!!!");

    else:
        with open("copy_donkey.txt", "w") as wr:
            wr.write(content);