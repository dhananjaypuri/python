listnew = [1,2,3,"hi","user", 6.5, 8 , 10, 11,12];
newlist = [];
for index,item in enumerate(listnew):
    if(index%2==0):
        newlist.append(item);

length = len(newlist);

print(newlist[0:4]);
