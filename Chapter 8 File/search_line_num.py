word = "donkey";
content = True;
i = 1;
with open("donkey.txt", "r") as f:
    while content:
        content = f.readline().lower();
        if word in content:
            print(f"{content} {i}");
        i += 1;    
            