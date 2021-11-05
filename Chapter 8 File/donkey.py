#Replace the word donkey

with open("donkey.txt", "r") as f:
    data = f.read();

if(data==""):
    print("File is empty!!!!!");
else:
    data = data.lower();
    newdata = data.replace("donkey", "######");   

    with open("donkey.txt", "w") as file:
        file.write(newdata);
    