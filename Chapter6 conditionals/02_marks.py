#Pass or Fail

m1 = int(input("Enter the marks of 1st Subjet : "));
m2 = int(input("Enter the marks of 2st Subjet : "));
m3 = int(input("Enter the marks of 3st Subjet : "));

if(m1<33 or m2<33 or m3<33):
    print("Sorry you failed in exam!!!!");

elif(((m1+m2+m3)/3)>40):
    print("You are Pass!!!!");
    
else:
    print("Sorry you failed in exam!!!!")