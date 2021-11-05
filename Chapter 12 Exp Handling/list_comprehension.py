a = [1,2,3,4,5,6,7,8,9,10];

# even = [];
# odd = [];

# for item in a:
#     if(item%2==0):
#         even.append(item);
#     else:
#         odd.append(item);

even = [i for i in a if(i%2==0)];  #This is a shortcut to the above commented lines
odd = [i for i in a if(i%2!=0)];   #This is a shortcut to the above commented lines

print(f"Even List : {even}");
print(f"Odd List : {odd}");