
listnew = [1,2.5,4,5,10,100,40,89,77,150];

newlist = [i for i in listnew if(i%5==0)];

print(newlist);

divisible = lambda a: a%5==0;

print(list(filter(divisible,listnew)));