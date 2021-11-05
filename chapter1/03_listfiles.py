#This program will return the list of files and directories in a directory.
import os

#If we specify the path then it will only gives the file names will not give . and ..
print(os.listdir('D:\\Study\\pythontut\\chapter1\\'));

#Will give all the files and directories if the path is not specified.
print(os.listdir());