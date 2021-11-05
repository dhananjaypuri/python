#Find a word in a file

f = open("file.txt", "r");
data = f.read().lower();

word = "twinkle";

result = data.count(word);

if(result>0):
    print(f"{word} is present !!!!");
else:
    print("Not Present");

f.close();