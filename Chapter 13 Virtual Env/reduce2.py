from functools import reduce;

listnew = [1,2.5,4,5,10,100,40,89,77,150];

max = lambda a,b: a>b;

val = reduce(max, listnew);

print(val);