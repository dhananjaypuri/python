# Detect Double Spaces

letter = "Hi  This is my  program.";

# This is will count the number of DoubleSpaces in the file 
print(letter.count("  "));

# This is will print the position of first DoubleSpaces in the file 
print(letter.find("  "));

# This will replace the space with $

letter = letter.replace(" ", "$");
print(letter);