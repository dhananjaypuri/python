# List Methods
newList = [10,20,3,4,5,6];

#Print Actual List
print(newList);

# Print Sorted List
newList.sort();
print(newList);

#Print the reverse List
newList.reverse();
print(newList);

#Append the list Adds the element at the end of the link
newList.append(60);
print(newList);

#Print the index at which the item is present in the list (first occurance)
print(newList.index(60));

#Insert the element at the mentioned index
newList.insert(2,300);
print(newList);

#This will delete the last element from the list
newList.pop(1);
print(newList);

#This will delete the first occurance of the element from the list
newList.remove(300);
print(newList);

#Delete all the elements from the list
newList.clear();
print(newList);