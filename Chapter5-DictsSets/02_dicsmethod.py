mydict = {
    "name": "Dhananjay Puri", "age": 32 , "marks": [1,3,4]
    };

#Print all the keys of the dictionary ==> dict_keys
print(mydict.keys());

#Convert the dict keys to list
print(list(mydict.keys()));

#Print all the values of the dictionary
print(mydict.values());

#Convery the dict_values keys to list
print(list(mydict.values()));

#Print all the items of the dictionary in a tuple form
print(mydict.items());
print(list(mydict.items()));

#Add the keys and value in dictionary
newdict = {
    "car": "Tata",
    "model": 2021
};
mydict.update(newdict); #Updates in dictionary
print(mydict);

#Print a value by key , but if the key is absent then it will return None

print(mydict.get("car"));