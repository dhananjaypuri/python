
num = int(input("Enter the number whose table is required : "));

table = [];

table = [i * num for i in range(1,11)];

#print(table);

newlist = [];

for item in table:
    newlist.append(str(item));

newstr = "\n".join(newlist);

print(newstr);