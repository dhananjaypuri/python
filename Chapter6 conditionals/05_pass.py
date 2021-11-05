#Pass or Fail

m1 = int(input("Enter the marks of 1st Subjet : "));
m2 = int(input("Enter the marks of 2st Subjet : "));
m3 = int(input("Enter the marks of 3st Subjet : "));

total = (m1+m2+m3)/3;

if(total>=90 and total<=100):
    print("Excellent!!!!");
elif(total>=80 and total<90):
    print("A Grade");    
elif(total>=70 and total<80):
    print("B Grade");   
elif(total>=60 and total<70):
    print("C Grade");
elif(total>=50 and total<60):
    print("C Grade");
elif(total<50):
    print("Sorry !!!!!!!!! You are fail");    
     
