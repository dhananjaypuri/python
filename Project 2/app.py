import random;

class Game:
    
    randNumber = random.randint(1,100);

    def guesss(self):

        userGuess = 0;
        print(self.randNumber);
        value = None;

        while(value != self.randNumber):
            value = int(input("Enter the number betweem 1 to 100 : "));

            if(value== self.randNumber ):

                print("Congrats !!!!! You Guessed it Correct !!!!!");
                break;

            else:

                userGuess += 1;
                chance = (3 - userGuess);

                print(f"Wrong Answer!!!! You have {chance} chances left");

                if(chance == 0):

                    print("Sorry You Loose !!!! Please try again !!!!!");
                    break;
                        


g1 = Game();

g1.guesss();

