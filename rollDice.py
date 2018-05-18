import random
def rollDice():
    roll = random.randrange(1, 6, 1);
    return roll;
    i=0  
for x in range(1, 100):
    roll = rollDice();
    arrayRolls[i]=[];
    i=i+1;
