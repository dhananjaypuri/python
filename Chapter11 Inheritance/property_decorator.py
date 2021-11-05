# class New:
#     a = 10;
#     b = 20;

#     def total(self):                #This is a replacement to @property in this we can make a function instead of property and it will work same
#         return self.a + self.b;
# n = New();
# print(n.total());

class New:

    salary = 5000;
    bonus = 1000;

    @property       # @property is doing a work of function but will be called as a variable
    def total(self):
        return self.salary + self.bonus;

n = New();

print(n.total);