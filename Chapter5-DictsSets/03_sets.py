#Set Syntax

set1 = {1,2,3,4};
print(set1); #Print Set

set1 = {1,2,3,4,1};
print(set1); #Note Repitative values cannot be stored in sets.

#How to create empty set
set2 = set();
print(set2);

#Add items to the empty set

set2.add(1);
set2.add(2);
print(set2);

#Remove the item from the set
set1.remove(1);
print(set1)

#Remove any random element from the set
set1.pop();
print(set1);