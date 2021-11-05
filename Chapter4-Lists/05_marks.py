marks = [];

m1 = input("Enter Marks for student 1 : ");
m2 = input("Enter Marks for student 2 : ");
m3 = input("Enter Marks for student 3 : ");

m1 = int(m1);
m2 = int(m2);
m3 = int(m3);

marks.append(m1);
marks.append(m2);
marks.append(m3);

marks.sort();

print(marks);