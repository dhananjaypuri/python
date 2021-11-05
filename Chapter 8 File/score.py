#High Score Up
import random;

randscore = random.randint(80,100);

with open("highscore.txt", "r") as f:
    data = f.read()

if (data==""):
    check = open("highscore.txt", "w");
    check.write(str(randscore));
    print("You are the highest Scorer!!!!!")
    check.close();
elif (randscore>int(data)):
    check = open("highscore.txt", "w");
    check.write(str(randscore));
    print("You are the highest Scorer!!!!!");
    check.close();
else:
    print(randscore);
    print("Sorry You Loose !!!!! Try Again !!!!!");

