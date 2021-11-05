                                        #Print table of a number in List
                                        
num = int(input("Enter the number : "));
table = [1,2,3,];

table = [i*num for i in range(1,11)]; #This command will add the table of the given number in the list

print(table);