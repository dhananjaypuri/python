#Prepare Table file

for item in range(2,11):
    with open(f"table/table_of_{item}.txt", "w") as f:
        for j in range(1,11):
            if(j==10):
                f.write(str(f"{item} * {j} = {item*j}"));
            else:    
                f.write(str(f"{item} * {j} = {item*j}\n"));
            