list1 = [2,4,5];

list2 = [i*i for i in list1];

print(list2);

##########################################

square = lambda input_list: input_list*input_list;

print(list(map(square,list1)));  # map(func,list) this will return a object , we have to typecast it into list