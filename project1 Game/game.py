#Snake , Water and Gun

import random;

def game(c,u):
    print("Computer : ", c);
    print("Player : ", u);
    if(c==u):
        result = None;
    elif(c=="W" and u=="G"):
        result = False
    elif(c=="S" and u=="G"):
        result = True;
    elif(c=="S" and u=="W"):
        result = True;    
    elif(c=="G" and u=="W" ):
        result = True;
    elif(c=="G" and u=="S" ):
        result = False;
    elif(c=="W" and u=="S"):
        result = False
    return result;

a = random.randint(1,3);
b = input("Player's Turn : Enter Snake(S), Water(W) or Gun(G) : ");

    
if(a==1):
    comp = "S";
elif(a==2):
    comp = "W";
elif(a==3):
    comp = "G";

# if (b=="S" or b!="W" or b!="G"):



winner = game(comp,b);

# print(winner);

if (winner==True):
    print("Congrats! You Win!!!!!!!");
elif(winner==None):
    print("This is a Tie!!!!!!!");
else:
    print("Sorry!! You loose ..");