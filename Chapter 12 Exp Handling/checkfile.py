import os.path as opath

# i = 1;
# while(i<=3):
#     with open(f"{i}.txt", "w") as f:
#         content = f"This is file {i}";
#         f.write(content);
#     i += 1;

filelist = ["1.txt","2.txt","3.txt"];

for item in filelist:
    if(opath.isfile(f"{item}")==True):
        print(f"{item} exists !!!!!");
    else:
        print(f"{item} does not exists !!!!!");