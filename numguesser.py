from random import randint


print("What shall the lower limit be [make sure it is an integer]: ")
lower = int(input("")) 

print("What shall the upper limit be [make sure it is an integer]: ")
upper = int(input("")) 

print("How many guesses should you get [make sure it is an integer]: ")
numofguess = int(input("")) 

num = randint(lower,upper)

print("Guess # 1 [make sure it is an integer]: ")
guess = int(input("")) 

i = 2
win = 0

while i <= numofguess:
    error = num-guess
    if error == 0:
        print("You win, your parents are proud")
        win = 1
        break
    elif error > 0:
        print("Higher")
    elif error < 0:
        print("Lower")
    print("Guess #",i," [make sure it is an integer]: ")    
    guess = int(input(""))
    i+=1
        
if win != 1:
    print("Sorry bruh, you lost")
