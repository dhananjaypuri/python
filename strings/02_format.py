# Print the formated string

strnew = '''Dear <|name|>,
            This is to inform you that you are selected!!!!
            Date: <|date|>''';
name = input("Enter the name : ");
date = input("Enter the Date : ");

strnew = strnew.replace("<|name|>", name);
strnew = strnew.replace("<|date|>", date);

print(strnew);