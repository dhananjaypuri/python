
from functools import reduce  # We have to import functool module in order to use Reduce function

listnew = [1,2,10,4,5,10,101,40,89,77];

max_num = reduce(max, listnew);
min_num = reduce(min, listnew);

print(max_num);
print(min_num);